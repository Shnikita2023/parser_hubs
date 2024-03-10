import os
from datetime import timedelta

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
app = Celery("app")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'run-every-10-minutes': {
        'task': 'articles.tasks.start_parser_task',
        'schedule': timedelta(minutes=10),
    },
}

