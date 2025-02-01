# 每日自动发布助手（DailyPost） 🌟

**每日自动发布助手** 是一个自动化工具，旨在帮助用户每天自动搜索相关领域的文章，经过 AI 润色后，自动发布到 CSDN、知乎、简书等平台。无论是技术分享、生活感悟还是行业动态，这个工具都能帮你轻松搞定！🚀

---
## 演示该功能


## 项目功能 🛠️

- **自动搜索文章**：根据用户设定的关键词，每天自动从互联网上抓取相关领域的优质文章。
- **AI 润色**：利用 AI 技术对抓取的文章进行润色，提升文章的可读性和专业性。
- **多平台发布**：支持一键发布到 CSDN、知乎、简书等多个内容平台，节省手动操作时间。
- **定时任务**：支持设置定时任务，每天自动执行，无需人工干预。
- **自定义配置**：用户可以根据自己的需求，配置关键词、发布频率、平台账号等信息。

---

## 技术栈 💻

- **编程语言**: Python
- **AI 模型**: OpenAI GPT / 其他自然语言处理模型
- **爬虫框架**: BeautifulSoup
- **自动化工具**: Selenium
- **任务调度**: Celery
- **平台 API**: CSDN、知乎、简书等平台

---

## 如何使用 🚀

### 1. 克隆项目
首先，将项目克隆到本地：
```bash
git clone https://github.com/Shy2593666979/DailyPost.git

cd DailyPost
```

### 2. 安装依赖
安装项目所需的依赖：
```
pip install -r requirements.txt
```
### 3. 配置参数
在 DailyPost/src/backend/.env 文件中创建并填写你的配置信息，例如：

```
BROKER = redis://localhost:6379/0
BACKEND = redis://localhost:6379/1

MODEL = gpt-4o-mini
API_KEY = your-api-key
BASE_URL = your-base-url

GOOGLE_KEY = your-google-key

USER_NAME = your-csdn-user
PASSWORD = your-csdn-passwd

EMAIL_TYPE = QQ
EMAIL_SENDER = your-qq-email
EMAIL_PASSWORD = your-qq-password
EMAIL_RECEIVERS = 2593666979@qq.com, 2490139200@qq.com, 1729188963@qq.com

RUN_TIME = 08:00

```

### 4. 运行项目
运行主程序，开始自动抓取、润色和发布：

```python
nohup python main.py &
```