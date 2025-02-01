
from search.combine import conform_article, write_local_md
from publish.publish_csdn import publisher
from publish.publish_email import emailer
from utils.helper import get_title
import subprocess
import os

# 启动 Celery Worker
def start_celery_worker():
    print("Starting Celery Worker...")
    worker_command = "celery -A tasks.celery_app worker --loglevel=info"
    subprocess.Popen(worker_command, shell=True, env=os.environ.copy())

# 启动 Celery Beat
def start_celery_beat():
    print("Starting Celery Beat...")
    beat_command = "celery -A tasks.celery_app beat --loglevel=info"
    subprocess.Popen(beat_command, shell=True, env=os.environ.copy())

def take_tasks():
    # 去相关网站上搜索相关文章
    content = conform_article()
    # 根据日期进行指定文章标题
    title = get_title()

    # 将文章保存到本地
    write_local_md(content)
    # 执行提交文章
    publisher.run(content, title)

    # 发送指定邮箱
    emailer.send_email(content, title)

if __name__ == '__main__':
    # 开启工作状态
    start_celery_worker()

    start_celery_beat()
