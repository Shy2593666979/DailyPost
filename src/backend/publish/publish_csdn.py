import time
from loguru import logger
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import setting
from publish.publish import AutoPublish


class AutoPublishCSDN(AutoPublish):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)


    # 登录 CSDN
    def login_csdn(self):

        self.driver.get("https://passport.csdn.net/login")

        # # 切换到账号密码登录
        time.sleep(3)
        login_button = self.driver.find_element(By.XPATH, "//span[contains(text(), '密码登录')]")
        login_button.click()

        time.sleep(3)
        # # 输入用户名和密码
        # username_input = driver.find_element(By.NAME, "loginName")
        # password_input = driver.find_element(By.NAME, "password")
        username_input = self.driver.find_element(By.XPATH, "//input[@autocomplete='username']")
        password_input = self.driver.find_element(By.XPATH, "//input[@autocomplete='current-password']")
        username_input.send_keys(self.username)
        password_input.send_keys(self.password)

        # # 点击登录按钮
        self.driver.find_element(By.XPATH, "//button[contains(text(), '登录')]").click()
        time.sleep(10)  # 等待登录完成

        try:
            iframe = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/iframe")
            self.driver.switch_to.frame(iframe)

            skip_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/button"))
            )

            # 点击“跳过”按钮
            skip_button.click()
            self.driver.switch_to.default_content()
            logger.info('----------登陆后发现弹窗, 已跳过-----------')
        except Exception as err:
            logger.info(f'登陆后发现弹窗, 出现问题: {err}')

        time.sleep(3)
        # for name, value in cookies.items():
        #     driver.add_cookie({"name": name, "value": value})
        #
        # driver.get("https://www.csdn.net/")
        # time.sleep(5)

        # 切换到密码登录方式（如果页面默认不是密码登录）
        # try:
        #     # 定位密码登录按钮并点击
        #     password_login_button = driver.find_element(By.XPATH, "//div[@class='login-select']/div[2]")
        #     password_login_button.click()
        # except Exception as e:
        #     print("密码登录按钮未找到或已处于密码登录模式。")

        # try:
        #     # 等待页面加载完成
        #     WebDriverWait(driver, 10).until(
        #         EC.presence_of_element_located((By.XPATH, "//div[contains(text(), '密码登录')]"))
        #     )
        #
        #     # 使用 JavaScript 切换到账号密码登录
        #     driver.execute_script("clickTabItemHandler('input');")
        #     time.sleep(5)  # 等待切换完成
        #
        #     # 输入用户名和密码
        #     username_input = WebDriverWait(driver, 10).until(
        #         EC.presence_of_element_located((By.NAME, "loginName"))
        #     )
        #     password_input = driver.find_element(By.NAME, "password")
        #     username_input.send_keys(username)
        #     password_input.send_keys(password)
        #
        #     # 点击登录按钮
        #     login_button = driver.find_element(By.XPATH, "//button[contains(text(), '登录')]")
        #     login_button.click()
        #     time.sleep(5)  # 等待登录完成
        # except Exception as e:
        #     print(f"登录失败: {e}")



    # 发布文章
    def publish_article(self, art_content, art_title):

        # 打开 CSDN 创作中心
        # writer_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div[6]')
        writer_button = self.driver.find_elements(By.XPATH, "//a[contains(text(), '创作')]")
        writer_button[1].click()

        time.sleep(5)

        # 这个是跳过是否体验新版创作者中心
        try:
            skip_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH,
                                                "/html/body/div[2]/div/div/div[1]/div[2]/section/div/div[1]/div/section/div[2]/div/div[2]/div[2]/button"))
            )

            # 点击“跳过”按钮
            skip_button.click()
            logger.info('----------登陆后发现弹窗, 已跳过-----------')
        except Exception as err:
            logger.info(f'登陆后发现弹窗, 出现问题: {err}')
        time.sleep(5)

        # 选择富文本编辑器
        check_md_button = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div[2]/section/div/div[1]/div/section/section/main/div/div/div/div/div/div/form/div[4]/div/span/span[2]/span[4]/span[3]/a[9]")
        check_md_button.click()
        time.sleep(3)

        # 获取所有窗口句柄
        window_handles = self.driver.window_handles

        # 切换到新标签页（最后一个句柄是新打开的标签页）
        self.driver.switch_to.window(window_handles[-1])
        time.sleep(3)

        # 输入标题
        title_input = self.driver.find_element(By.XPATH, "//input[contains(@placeholder, '文章标题')]")
        title_input.clear()
        title_input.send_keys(art_title)
        time.sleep(5)

        # 输入内容
        # iframe = self.driver.find_element(By.CSS_SELECTOR, "iframe.cke_wysiwyg_frame")
        # self.driver.switch_to.frame(iframe)
        content_input = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div[1]/div[2]/pre/div[1]/span[1]")
        # content_input.clear()
        actions = ActionChains(self.driver)
        actions.click(content_input)  # 确保点击输入框以获得焦点
        actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()
        # content_input.send_keys(Keys.CONTROL, 'a')  # 全选
        # content_input.send_keys(Keys.DELETE)  # 删除选中的内容
        # self.driver.execute_script(f"arguments[0].value = '{art_content}';", content_input)
        time.sleep(1)
        content_input = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div[1]/div[2]/pre/div[1]/span[1]")
        content_input.send_keys(art_content)
        # content_input.send_keys(art_content)
        # element = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, "body[contenteditable='true']"))
        # )
        # element.send_keys(content)
        # editable_area = driver.find_element(By.XPATH, "/html/body")
        # editable_area.send_keys("这是我的创作内容")  # 输入文本
        # script = """
        #         var body = document.querySelector("body[contenteditable='true']")
        #         body.textContent = "这是我的创作内容";  // 替换为纯文本
        #         // 或者使用 innerHTML 设置富文本
        #         // body.innerHTML = "<strong>加粗文本</strong> <em>斜体文本</em>";
        #     """
        # driver.execute_script(script)

        # 使用 JavaScript 缩小浏览器界面

        # 跳出 iframe，回到主文档
        # self.driver.switch_to.default_content()

        # ----------------------------
        # add_tag = self.driver.find_element(By.XPATH,
        #                               "/html/body/div[2]/div/div/div[1]/div[2]/section/div/div[1]/div/section/section/main/div/div/div/div/div/div/form/div[5]/div[1]/div/div/div[1]/button")
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", add_tag)
        # add_tag.click()
        # logger.info('----------点击文章标签正确-----------')
        #
        # time.sleep(1)
        #
        # first_tag = self.driver.find_element(By.XPATH,
        #                                 "/html/body/div[2]/div/div/div[1]/div[2]/section/div/div[1]/div/section/section/main/div/div/div/div/div/div/form/div[5]/div[1]/div/div/div[2]/div[4]/div/div[1]/div/div/div/div[35]")
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", first_tag)
        # first_tag.click()
        # logger.info('----------选择标签大类正确-----------')
        #
        # time.sleep(1)
        #
        # second_tag = self.driver.find_element(By.XPATH,
        #                                  "/html/body/div[2]/div/div/div[1]/div[2]/section/div/div[1]/div/section/section/main/div/div/div/div/div/div/form/div[5]/div[1]/div/div/div[2]/div[4]/div/div[2]/div[35]/span[1]")
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", second_tag)
        # second_tag.click()
        # logger.info('----------选择标具体标签正确-----------')

        # 直接选择发布
        time.sleep(5)
        publish_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "/html/body/div[1]/div[1]/div[1]/div/div[3]/button[2]"))
        )
        publish_button.click()
        time.sleep(3)

        # 点击文章的标签
        add_tag = self.driver.find_element(By.XPATH,
                                      "/html/body/div[1]/div[2]/div/div[1]/div[1]/div[1]/div/div/div/button")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", add_tag)
        add_tag.click()
        logger.info('----------点击文章标签正确-----------')
        time.sleep(1)

        # 选择表现的大类
        first_tag = self.driver.find_element(By.XPATH,
                                        "/html/body/div[1]/div[2]/div/div[1]/div[1]/div[1]/div/div/div[2]/div[4]/div/ul/li[30]")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", first_tag)
        first_tag.click()
        logger.info('----------选择标签大类正确-----------')
        time.sleep(1)

        # 选择的是具体的标签
        second_tag = self.driver.find_element(By.XPATH,
                                         "/html/body/div[1]/div[2]/div/div[1]/div[1]/div[1]/div/div/div[2]/div[4]/div/div/div[2]/span[7]")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", second_tag)
        second_tag.click()
        logger.info('----------选择标具体标签正确-----------')
        time.sleep(1)

        close_btn = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div[1]/div[1]/div/div/div[2]/div[4]/button")
        close_btn.click()
        time.sleep(2)

        abstract_input = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div[1]/div[3]/div/div[1]/textarea")
        abstract_input.send_keys(art_title)
        time.sleep(1)

        # 最终的发布
        final_publish = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div[2]/button[4]")
        final_publish.click()

        time.sleep(5)

    def run(self, content, title):
        self.driver = AutoPublish.init_driver()

        self.login_csdn()

        self.publish_article(content, title)

        # 关闭浏览器
        self.driver.quit()

publisher = AutoPublishCSDN(**setting.dict())


if __name__ == '__main__':
    publisher.run("## 你好啊")







    # # 主函数
    # def main():
    #     # 本地 Markdown 文件路径
    #     md_file_path = "123.md"
    #
    #     # 读取 Markdown 文件
    #     md_content = read_markdown_file(md_file_path)
    #
    #     # 初始化浏览器
    #     driver = init_driver()
    #
    #     try:
    #         # 登录 CSDN
    #         login_csdn(driver, "15937374105", "mingguang0703..")
    #
    #         # 发布文章
    #         publish_article(driver, "你的文章标题", md_content)
    #         logger.info("----------文章发布成功！------------")
    #     except Exception as e:
    #         print(f"发布失败: {e}")
    #     finally:
    #         # 关闭浏览器
    #         driver.quit()
    #
    # if __name__ == "__main__":
    #     main()

    # # 登录知乎
    # def login_zhihu(driver, username, password):
    #     driver.get("https://passport.csdn.net/login")
    #     time.sleep(2)
    #
    #     # 切换到密码登录
    #     driver.find_element(By.XPATH, "//div[@class='SignFlow-tab']").click()
    #     time.sleep(1)
    #
    #     # 输入用户名和密码
    #     username_input = driver.find_element(By.NAME, "loginName")
    #     password_input = driver.find_element(By.NAME, "password")
    #     username_input.send_keys(username)
    #     password_input.send_keys(password)
    #
    #     # 点击登录按钮
    #     driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #     input("请在浏览器中完成验证码验证，然后按回车继续...")
    #     time.sleep(5)  # 等待登录完成
    #
    # # 发布文章
    # def publish_article(driver, title, content):
    #     # 打开知乎创作中心
    #     driver.get("https://zhuanlan.zhihu.com/write")
    #     time.sleep(5)
    #
    #     # 输入标题
    #     title_input = driver.find_element(By.XPATH, "//textarea[@placeholder='请输入标题']")
    #     title_input.send_keys(title)
    #
    #     # 输入内容
    #     content_input = driver.find_element(By.XPATH, "//div[@role='textbox']")
    #     content_input.send_keys(content)
    #
    #     # 点击发布按钮
    #     publish_button = WebDriverWait(driver, 10).until(
    #         EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), '发布')]"))
    #     )
    #     publish_button.click()
    #     time.sleep(5)
    #
    # # 主函数
    # def main():
    #     # 本地 Markdown 文件路径
    #     md_file_path = "123.md"
    #
    #     # 读取 Markdown 文件
    #     md_content = read_markdown_file(md_file_path)
    #
    #     # 初始化浏览器
    #     driver = init_driver()
    #
    #     try:
    #         # 登录知乎
    #         login_zhihu(driver, "15937374105", "mingguang0703..")
    #
    #         # 发布文章
    #         publish_article(driver, "你的文章标题", md_content)
    #         print("文章发布成功！")
    #     except Exception as e:
    #         print(f"发布失败: {e}")
    #     finally:
    #         # 关闭浏览器
    #         driver.quit()
    #
    # if __name__ == "__main__":
    #     main()
