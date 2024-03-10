from typing import Optional, Any

from django.core.exceptions import ObjectDoesNotExist

from hubs.models import Hub
from .models import Article
from logging_config import MyLogger

logger = MyLogger(pathname=__name__).init_logger


class ArticleService:
    """
    Сервис статей
    """

    @classmethod
    async def add_article(cls,
                          title: str,
                          date: str,
                          content: str,
                          author_name: str,
                          author_link: str,
                          article_link: str,
                          hub: Hub) -> None:
        existing_arcticle: Optional[Article] = await cls.get_article(article_link=article_link)

        if existing_arcticle:
            return

        new_article: dict[str, Any] = {"title": title,
                                       "date": date,
                                       "content": content,
                                       "author_name": author_name,
                                       "article_link": article_link,
                                       "author_link": author_link,
                                       "hub": hub}
        await Article.objects.acreate(**new_article)
        logger.info(msg=f"Добавлена статья '{new_article['title']}' в БД")

    @staticmethod
    async def get_article(article_link: str) -> Optional[Article]:
        try:
            return await Article.objects.aget(article_link=article_link)
        except ObjectDoesNotExist:
            return None


article_service: ArticleService = ArticleService()
