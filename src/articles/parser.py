import asyncio
from asyncio import Semaphore
from typing import Any, Generator, Optional

from bs4 import BeautifulSoup

from articles.services import article_service
from http_client.aiohttp_client import AiohttpClient
from http_client.http_client_interface import HTTPClientInterface
from hubs.models import Hub
from hubs.services import hub_service
from logging_config import MyLogger

logger = MyLogger(pathname=__name__).init_logger


class ArticlesManager:
    """
    Менеджер статей
    """

    URL_HABR: str = "https://habr.com"

    def __init__(self, http_client: HTTPClientInterface) -> None:
        self.http_client: HTTPClientInterface = http_client

    async def fetch_data_article(self, url: str, semaphore: Semaphore, model_hub: Hub) -> None:
        async with semaphore:
            response_html: Optional[str] = await self.http_client.get(url=url)
            if response_html:
                soup: BeautifulSoup = BeautifulSoup(response_html, "html.parser")
                title: str = soup.find("h1", class_="tm-title tm-title_h1").text.strip()
                date: str = soup.find("span", class_="tm-article-datetime-published").text.strip()
                content: str = soup.find("div", class_="tm-article-body").text.strip()
                author_name: str = soup.find("a", class_="tm-user-info__username").text.strip()
                author_link: str = soup.find("a", class_="tm-user-info__username").get("href")
                await article_service.add_article(title, date, content, author_name, author_link, url, model_hub)
                print(f"Название статьи: {title}, Дата публикации: {date}, Ссылка на пост: {url}"
                      f" Автор: {author_name}, Ссылка на автора: {self.URL_HABR}{author_link}")

            return None

    async def get_url_articles(self) -> None:
        logger.info("Ожидайте идёт процесс парсинга...")
        models_hubs: list[Hub] = await hub_service.get_hubs()
        for hub in models_hubs:
            response_html: Optional[str] = await self.http_client.get(url=hub.hub_link)
            soup: BeautifulSoup = BeautifulSoup(response_html, 'html.parser')
            article_links: Generator[str, Any, None] = (self.URL_HABR + a.get('href') for a in
                                                        soup.find_all('a', class_='tm-title__link'))
            await self.create_tasks(model_hub=hub, article_links=article_links)
        logger.info("Парсинг успешно завершён!")

    async def create_tasks(self,
                           model_hub: Hub,
                           article_links: Generator[str | Any, Any, None]) -> None:
        semaphore: Semaphore = Semaphore(5)
        tasks: list = []
        for link in article_links:
            tasks.append(self.fetch_data_article(url=link, semaphore=semaphore, model_hub=model_hub))
        await asyncio.gather(*tasks)


client: AiohttpClient = AiohttpClient()
articles_manager: ArticlesManager = ArticlesManager(client)
