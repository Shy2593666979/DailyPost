import asyncio
import json
import time

import requests
from loguru import logger
from bs4 import BeautifulSoup

from llm.chat import chat_llm
from search.news_ai import search_news_ai
from search.news_sina import search_news_sina
from search.news_finance import search_news_finance


# 将三种类型的新闻合并
def combine_news():
    total_news = []
    total_news += search_news_ai()

    # 以下两个新闻有关政治，可能有些文章或者模型会出问题
    # total_news += search_news_finance()
    # total_news += search_news_sina()

    result = []
    for news in total_news:
        url = news['url']
        text = request_url(url)
        result.append({'url': url, 'text': text})

    return result

async def async_chat_llm(query):
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, chat_llm.chat, query)
    return result

async def exec_chat():
    news_result = combine_news()
    prompt_result = []

    for res in news_result:
        prompt_result.append(summary_prompt.format(text=res['text']))

    tasks = [async_chat_llm(prompt) for prompt in prompt_result]
    results = await asyncio.gather(*tasks)

    json_results = []
    for res in results:
        if json_text:= resolve_text(res):
            json_results.append(json_text)
    return json_results

def resolve_text(text):
    try:
        text = json.loads(text)
        return {'type': text['type'], 'title': text['title'], 'text': text['text']}
    except Exception as err:
        logger.error(f'{text} is not json error: {err}')


def request_url(url: str):
    response = requests.get(url)

    if response.status_code == 200:
        response.encoding = 'UTF-8'

        soup = BeautifulSoup(response.text, "html.parser")
        return soup.get_text().strip()
    else:
        logger.info('This web not found content')
        return ''

def conform_article():
    news_json = asyncio.run(exec_chat())

    results_json = {}

    for news in news_json:
        if news['type'] in results_json:
            results_json[news['type']].append({'title': news['title'], 'text': news['text']})
        else:
            results_json[news['type']] = [{'title': news['title'], 'text': news['text']}]

    publish_article = article_scheme_md
    for key, values in results_json.items():
        publish_article += f"## {key}快讯\n\n"
        for val in values:
            publish_article += f"### {val['title']} \n"
            publish_article += f"{val['text']} \n\n"

    return publish_article

def write_local_md(content):
    current_date = time.strftime("%m月%d日", time.localtime())
    with open(f'docs/{current_date}.md', 'w', encoding='UTF-8') as file:
        file.write(content)

    logger.info(f'{current_date}的文章已保存到本地')

def write_local_docx(content):
    current_date = time.strftime("%m月%d日", time.localtime())
    with open(f'docs/{current_date}.docx', 'w', encoding='UTF-8') as file:
        file.write(content)

    logger.info(f'{current_date}的文章已保存到本地')

summary_prompt = """
## 角色 
你现在是一个总结新闻的助手

## 任务
你的任务是根据提供的文章内容生成（文章标题、文章概括、文章类型）

## 生成格式
{{"type": "科技", "title": "AI以后会成为主要生产力吗？", "text": "AI的发展迅速，为我们带来了很多的便捷........"}}

type 是文章的类型，例如：科技、金融、娱乐、军事
title 是文章的标题
text 是文章的概括

## 文章内容：
{text}
"""

article_scheme_md = """

# 今日快讯 (DailyPost)

"""

article_scheme_docx = """
今日快讯 (DailyPost)

"""

if __name__ == '__main__':
    conform_article()
