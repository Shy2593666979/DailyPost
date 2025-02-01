from loguru import logger
from openai import OpenAI
from config import setting


class ChatLLM:
    def __init__(self):
        self.client = OpenAI(api_key=setting.API_KEY, base_url=setting.BASE_URL)
        self.model = setting.MODEL


    def chat(self, query: str):
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant"},
                    {"role": "user", "content": query},
                ], stream=False)

            return response.choices[0].message.content
        except Exception as err:
            logger.error(f'llm chat appear error: {err}')
            return {'type': "新闻", 'title': "标题", 'text': "文本内容"}

chat_llm = ChatLLM()
