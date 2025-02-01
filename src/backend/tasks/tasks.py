from tasks.celery_app import app
from main import take_tasks

@app.task
def publish_art():
    take_tasks()