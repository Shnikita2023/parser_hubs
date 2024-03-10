from asgiref.sync import async_to_sync

from app.celery import app
from articles.parser import articles_manager


@app.task()
def start_parser_task() -> None:
    async_to_sync(articles_manager.get_url_articles)()
