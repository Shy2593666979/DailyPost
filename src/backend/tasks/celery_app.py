from celery import Celery
from celery.schedules import crontab
from config import setting

app = Celery("DailyPost",
             include=['tasks.tasks'],
             broker=setting.BROKER,
             backend=setting.BACKEND)


# 配置时区
app.conf.timezone = setting.TIME_ZONE

run_time_hour = setting.RUN_TIME.split(':')[0]
run_time_minute = setting.RUN_TIME.split(':')[1]

# 加载定时任务配置
app.conf.beat_schedule = {
    'daily-morning-task': {
        'task': 'tasks.publish_art',  # 任务路径
        'schedule': crontab(hour=run_time_hour, minute=run_time_minute),  # 每天早上 8 点运行
    },
}