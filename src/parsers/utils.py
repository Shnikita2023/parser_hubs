import locale
from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from typing import TypeVar

from logging_config import MyLogger

locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')

logger = MyLogger(pathname=__name__).init_logger


class DateParser(ABC):
    @abstractmethod
    def convert_date(self, date_str: str, current_date_time: datetime) -> None:
        raise NotImplementedError


class YesterdayDateParser(DateParser):
    def convert_date(self, date_str: str, current_date_time: datetime) -> datetime:
        date_time = datetime.strptime(date_str, "вчера в %H:%M")
        return (current_date_time - timedelta(days=1)).replace(hour=date_time.hour,
                                                               minute=date_time.minute,
                                                               second=0,
                                                               microsecond=0)


class HourDateParser(DateParser):
    def convert_date(self, date_str: str, current_date_time: datetime) -> datetime:
        hours = int(date_str.split()[0])
        return (current_date_time - timedelta(hours=hours)).replace(microsecond=0)


class MinuteDateParser(DateParser):
    def convert_date(self, date_str: str, current_date_time: datetime) -> datetime:
        minutes = int(date_str.split()[0])
        return (current_date_time - timedelta(minutes=minutes)).replace(microsecond=0)


class YearDateParser(DateParser):
    def convert_date(self, date_str: str, current_date_time: datetime) -> datetime:
        return datetime.strptime(date_str, "%d %b %Y в %H:%M")


class NotYearDateParser(DateParser):
    def convert_date(self, date_str: str, current_date_time: datetime) -> datetime:
        date_time = datetime.strptime(date_str, "%d %b в %H:%M").replace(year=current_date_time.year)
        return date_time.replace(year=current_date_time.year)


T = TypeVar('T',
            YesterdayDateParser,
            HourDateParser,
            MinuteDateParser,
            YearDateParser,
            NotYearDateParser,
            )


class DateTimeConverterFactory:
    @staticmethod
    def create_date_parser(date_str: str) -> T:
        try:
            list_datetime = date_str.split()
            if list_datetime[0] == "вчера":
                return YesterdayDateParser()
            elif "час" in list_datetime[1]:
                return HourDateParser()
            elif "мин" in list_datetime[1]:
                return MinuteDateParser()
            elif list_datetime[2].isdigit():
                return YearDateParser()
            else:
                return NotYearDateParser()

        except ValueError as ex:
            logger.error(msg="Неверный формат данных", exc_info=ex)


class DateTimeConverter:

    def __init__(self, date_str: str) -> None:
        self.current_date_time: datetime = datetime.now()
        self.date_str: str = date_str

    async def convert_stroka_with_datetime(self) -> datetime:
        parser: T = DateTimeConverterFactory.create_date_parser(self.date_str)
        return parser.convert_date(self.date_str, self.current_date_time)
