import time
from loguru import logger
from selenium import webdriver


class AutoPublish:
    def __init__(self, **kwargs):
        self.driver = None
        self.username = kwargs.get('USER_NAME')
        self.password = kwargs.get('PASSWORD')



    # 初始化 Selenium WebDriver
    @staticmethod
    def init_driver():
        # 使用 webdriver-manager 自动下载 ChromeDriver
        # service = Service(EdgeChromiumDriverManager().install())
        # service = Service(GeckoDriverManager().install())
        # options = webdriver.FirefoxOptions()  # 火狐浏览器
        # options = webdriver.EdgeOptions()     # Edge
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--headless")
        options.add_argument("--start-maximized")  # 最大化浏览器窗口
        options.add_argument("--force-device-scale-factor=0.6")  # 缩小浏览器比例
        # driver = webdriver.Edge(service=service, options=options)
        # driver = webdriver.Firefox(service=service, options=options)
        driver = webdriver.Chrome(options=options)
        return driver

    @staticmethod
    def init_title_content(art_content):

        # # 读取本地 Markdown 文件
        # def read_markdown_file(path):
        #     with open(path, 'r', encoding='utf-8') as file:
        #         return file.read()

        pass

