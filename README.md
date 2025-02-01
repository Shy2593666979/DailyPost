# 每日自动发布助手（DailyPost） 🌟

**每日自动发布助手** 是一个自动化工具，旨在帮助用户每天自动搜索相关领域的文章，经过 AI 润色后，自动发布到 CSDN、知乎、简书等平台。无论是技术分享、生活感悟还是行业动态，这个工具都能帮你轻松搞定！🚀

---
## 演示项目
![DailyPost_1](https://github.com/user-attachments/assets/1bb18324-420a-47aa-9130-48bd79b33487)


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
#### 安装Python所需的依赖：
```
pip install -r requirements.txt
```
#### 项目依赖

Redis

Google-Chrome

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

## 日志文件

```bash
Starting Celery Worker...
Starting Celery Beat...
/root/miniconda3/envs/DailyPost/lib/python3.10/site-packages/celery/platforms.py:829: SecurityWarning: You're running the worker with superuser privileges: this is
absolutely not recommended!

Please specify a different user using the --uid option.

User information: uid=0 euid=0 gid=0 egid=0

  warnings.warn(SecurityWarning(ROOT_DISCOURAGED.format(
[2025-02-01 19:11:33,522: INFO/MainProcess] beat: Starting...
 
 -------------- celery@autodl-container-d5c045a32e-3af1d863 v5.4.0 (opalescent)
--- ***** ----- 
-- ******* ---- Linux-5.4.0-153-generic-x86_64-with-glibc2.35 2025-02-01 19:11:33
- *** --- * --- 
- ** ---------- [config]
- ** ---------- .> app:         DailyPost:0x7f5b0712a980
- ** ---------- .> transport:   redis://localhost:6379/0
- ** ---------- .> results:     redis://localhost:6379/1
- *** --- * --- .> concurrency: 128 (prefork)
-- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
--- ***** ----- 
 -------------- [queues]
                .> celery           exchange=celery(direct) key=celery
                

[tasks]
  . tasks.tasks.publish_art

[2025-02-01 19:11:38,680: WARNING/MainProcess] /root/miniconda3/envs/DailyPost/lib/python3.10/site-packages/celery/worker/consumer/consumer.py:508: CPendingDeprecationWarning: The broker_connection_retry configuration setting will no longer determine
whether broker connection retries are made during startup in Celery 6.0 and above.
If you wish to retain the existing behavior for retrying connections on startup,
you should set broker_connection_retry_on_startup to True.
  warnings.warn(

[2025-02-01 19:11:38,687: INFO/MainProcess] Connected to redis://localhost:6379/0
[2025-02-01 19:11:38,688: WARNING/MainProcess] /root/miniconda3/envs/DailyPost/lib/python3.10/site-packages/celery/worker/consumer/consumer.py:508: CPendingDeprecationWarning: The broker_connection_retry configuration setting will no longer determine
whether broker connection retries are made during startup in Celery 6.0 and above.
If you wish to retain the existing behavior for retrying connections on startup,
you should set broker_connection_retry_on_startup to True.
  warnings.warn(

[2025-02-01 19:11:38,690: INFO/MainProcess] mingle: searching for neighbors
[2025-02-01 19:11:39,700: WARNING/MainProcess] /root/miniconda3/envs/DailyPost/lib/python3.10/site-packages/celery/app/control.py:56: DuplicateNodenameWarning: Received multiple replies from node name: celery@autodl-container-d5c045a32e-3af1d863.
Please make sure you give each node a unique nodename using
the celery worker `-n` option.
  warnings.warn(DuplicateNodenameWarning(

[2025-02-01 19:11:39,700: INFO/MainProcess] mingle: all alone
[2025-02-01 19:11:39,713: INFO/MainProcess] celery@autodl-container-d5c045a32e-3af1d863 ready.
[2025-02-01 19:15:00,094: INFO/MainProcess] Scheduler: Sending due task daily-morning-task (tasks.tasks.publish_art)
[2025-02-01 19:15:00,105: INFO/MainProcess] Task tasks.tasks.publish_art[77df9d42-f929-473b-8739-d3f58bb70f46] received
[2025-02-01 19:15:08,688: INFO/ForkPoolWorker-128] HTTP Request: POST https://api.openai-proxy.org/v1/chat/completions "HTTP/1.1 200 OK"
[2025-02-01 19:15:08,699: INFO/ForkPoolWorker-128] HTTP Request: POST https://api.openai-proxy.org/v1/chat/completions "HTTP/1.1 200 OK"
[2025-02-01 19:15:08,754: INFO/ForkPoolWorker-128] HTTP Request: POST https://api.openai-proxy.org/v1/chat/completions "HTTP/1.1 200 OK"
[2025-02-01 19:15:08,942: INFO/ForkPoolWorker-128] HTTP Request: POST https://api.openai-proxy.org/v1/chat/completions "HTTP/1.1 200 OK"
[2025-02-01 19:15:09,220: INFO/ForkPoolWorker-128] HTTP Request: POST https://api.openai-proxy.org/v1/chat/completions "HTTP/1.1 200 OK"
[2025-02-01 19:15:09,478: INFO/ForkPoolWorker-128] HTTP Request: POST https://api.openai-proxy.org/v1/chat/completions "HTTP/1.1 200 OK"
[2025-02-01 19:15:09,778: INFO/ForkPoolWorker-128] HTTP Request: POST https://api.openai-proxy.org/v1/chat/completions "HTTP/1.1 200 OK"
[2025-02-01 19:15:10,523: INFO/ForkPoolWorker-128] HTTP Request: POST https://api.openai-proxy.org/v1/chat/completions "HTTP/1.1 200 OK"
[2025-02-01 19:15:11,692: INFO/ForkPoolWorker-128] HTTP Request: POST https://api.openai-proxy.org/v1/chat/completions "HTTP/1.1 200 OK"
[2025-02-01 19:15:13,255: INFO/ForkPoolWorker-128] HTTP Request: POST https://api.openai-proxy.org/v1/chat/completions "HTTP/1.1 200 OK"
2025-02-01 19:15:13.260 | INFO     | search.combine:write_local_md:98 - 02月01日的文章已保存到本地
2025-02-01 19:15:30.902 | INFO     | publish.publish_csdn:login_csdn:56 - ----------登陆后发现弹窗, 已跳过-----------
2025-02-01 19:15:49.792 | INFO     | publish.publish_csdn:publish_article:123 - 登陆后发现弹窗, 出现问题: Message: 
Stacktrace:
#0 0x55b3abe6553a <unknown>
#1 0x55b3ab960f00 <unknown>
#2 0x55b3ab9b0c0c <unknown>
#3 0x55b3ab9b0e31 <unknown>
#4 0x55b3ab9f6bd4 <unknown>
#5 0x55b3ab9d55cd <unknown>
#6 0x55b3ab9f3f84 <unknown>
#7 0x55b3ab9d5343 <unknown>
#8 0x55b3ab9a278a <unknown>
#9 0x55b3ab9a39de <unknown>
#10 0x55b3abe2f2cb <unknown>
#11 0x55b3abe33242 <unknown>
#12 0x55b3abe1c7ac <unknown>
#13 0x55b3abe33df7 <unknown>
#14 0x55b3abe00b2f <unknown>
#15 0x55b3abe541a8 <unknown>
#16 0x55b3abe54370 <unknown>
#17 0x55b3abe643b6 <unknown>
#18 0x7f4263ba6ac3 <unknown>

2025-02-01 19:16:24.457 | INFO     | publish.publish_csdn:publish_article:215 - ----------点击文章标签正确-----------
2025-02-01 19:16:25.568 | INFO     | publish.publish_csdn:publish_article:223 - ----------选择标签大类正确-----------
2025-02-01 19:16:26.675 | INFO     | publish.publish_csdn:publish_article:231 - ----------选择标具体标签正确-----------
2025-02-01 19:16:37.028 | INFO     | publish.publish_email:_send:54 - sender: 2593666979@qq.com, receiver: 2593666979@qq.com
2025-02-01 19:16:37.993 | INFO     | publish.publish_email:_send:54 - sender: 2593666979@qq.com, receiver:  2490139200@qq.com
2025-02-01 19:16:38.896 | INFO     | publish.publish_email:_send:54 - sender: 2593666979@qq.com, receiver:  1729188963@qq.com
[2025-02-01 19:16:38,942: INFO/ForkPoolWorker-128] Task tasks.tasks.publish_art[77df9d42-f929-473b-8739-d3f58bb70f46] succeeded in 98.83521770872176s: None

```
