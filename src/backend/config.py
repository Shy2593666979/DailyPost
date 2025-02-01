from typing import List
from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    # celery配置
    BROKER: str
    BACKEND: str

    # LLM 配置
    MODEL: str
    API_KEY: str
    BASE_URL: str

    # 搜索引擎Google
    GOOGLE_KEY: str

    # CSDN配置
    USER_NAME: str
    PASSWORD: str

    # Email 配置
    EMAIL_TYPE: str
    EMAIL_SENDER: str
    EMAIL_PASSWORD: str
    EMAIL_RECEIVERS: List[str]

    # 爬取网站
    AI_NEWS_URL: str = "https://www.aibase.com/zh/news"
    AI_NEWS_K: int = 10

    FINANCE_NEWS_URL: str = "https://finance.caijing.com.cn/"
    FINANCE_NEWS_K: int = 10

    SINA_NEWS_URL: str = "https://news.sina.com.cn/"
    SINA_NEWS_K: int = 10


    # 时区
    TIME_ZONE: str = "Asia/Shanghai"

    # 运行时间
    RUN_TIME: str

    class Config:

        @classmethod
        def parse_env_var(cls, field_name: str, raw_val: str):
            if field_name == "EMAIL_RECEIVERS":
                return raw_val.split(",")
            return cls.json_loads(raw_val)

setting = Settings(_env_file=".env")
