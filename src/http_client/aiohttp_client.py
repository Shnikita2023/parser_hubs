from typing import Optional

import aiohttp

from http_client.http_client_interface import HTTPClientInterface
from logging_config import MyLogger

logger = MyLogger(pathname=__name__).init_logger


class AiohttpClient(HTTPClientInterface):

    async def get(self, url: str) -> Optional[str]:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:

                    if response.status != 200:
                        raise aiohttp.ClientError(f"Ошибка при получении данных: Status {response.status}")

                    html: Optional[str] = await response.text()

            return html

        except aiohttp.ClientError as ex:
            logger.critical(msg=f"Что-то пошло не так, попробуйте позже: {ex}")

