import logging


class MyLogger:

    def __init__(self,
                 pathname: str = '',
                 name_logger: str = "parser_logger",
                 filename: str = "parsers.log"):
        self.pathname = pathname
        self.logger = logging.getLogger(name_logger)
        self.filename = filename

    @property
    def init_logger(self):
        logging.basicConfig(
            level=logging.INFO,
            format=f"%(asctime)s :: %(levelname)s :: {self.pathname}:%(lineno)d - %(message)s",
            handlers=[
                logging.FileHandler(filename=self.filename, mode="w", encoding="utf-8"),
                logging.StreamHandler()
            ]
        )
        return self.logger
