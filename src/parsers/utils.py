import locale
from datetime import datetime, timedelta

from logging_config import MyLogger

locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')

logger = MyLogger(pathname=__name__).init_logger


class DateTimeConverter:
    def __init__(self, date_str: str):
        self.date_str: str = date_str

    async def convert_stroka_with_datetime(self) -> datetime:
        try:
            list_datetime: list = self.date_str.split()
            current_date_time: datetime = datetime.now()

            if list_datetime[0] == "вчера":
                date_time = datetime.strptime(self.date_str, "вчера в %H:%M")
                formatted_date_time = (current_date_time - timedelta(days=1)).replace(hour=date_time.hour,
                                                                                      minute=date_time.minute,
                                                                                      second=0,
                                                                                      microsecond=0)

            elif "час" in list_datetime[1]:
                formatted_date_time = ((current_date_time - timedelta(hours=int(list_datetime[0]))).
                                       replace(microsecond=0))

            elif "мин" in list_datetime[1]:
                formatted_date_time = ((current_date_time - timedelta(minutes=int(list_datetime[0]))).
                                       replace(microsecond=0))

            elif list_datetime[2].isdigit():
                formatted_date_time = datetime.strptime(self.date_str, "%d %b %Y в %H:%M")

            else:
                date_time = datetime.strptime(self.date_str, "%d %b в %H:%M").replace(year=current_date_time.year)
                formatted_date_time = date_time.replace(year=current_date_time.year)

            return formatted_date_time

        except ValueError as ex:
            logger.error(msg="Неверный формат данных", exc_info=ex)

