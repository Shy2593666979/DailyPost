import requests
from loguru import logger

from config import setting
from bs4 import BeautifulSoup


def search_news_ai():
    # 发送HTTP GET请求
    response = requests.get(setting.AI_NEWS_URL)

    result = []
    # 检查请求是否成功
    if response.status_code == 200:
        # 解析HTML内容
        soup = BeautifulSoup(response.text, 'html.parser')

        # 提取所有带有超链接的文本
        links = soup.find_all('a')  # 找到所有 <a> 标签

        # 遍历每个链接并提取文本和URL
        for link in links:
            text = link.get_text(strip=True)  # 提取链接的文本内容
            href = link.get('href')  # 提取链接的URL
            if text and href:  # 确保文本和URL都存在
                href_list = href.split('/')
                news_id = href_list[-1]

                # 去除文本的杂质
                text = text.replace('AIbase', '')
                if news_id.isnumeric():
                    result.append({'text': text, 'url': setting.AI_NEWS_URL + f"/{news_id}"})
                if len(result) == setting.AI_NEWS_K:
                    break
        return result
    else:
        logger.info(f"Failed to retrieve the website. Status code: {response.status_code}")
        return result

if __name__ == "__main__":
    print(search_news_ai())