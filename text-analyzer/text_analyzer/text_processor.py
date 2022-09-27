import logging
from typing import Union
import requests
from collections import namedtuple
from functools import cached_property
from text_analyzer import TextAnalyzer
from db.repository import Repository

Source = namedtuple("Source", ["type", "value"])


class TextProcessor:
    def __init__(self, source: Source, repository: Repository) -> None:
        self.source = source
        self.repository = repository

    def analyze(self) -> None:
        self.logger.info("Started getting text")

        if self.source.type == "r":
            text = self.load_text_from_url()
        elif self.source.type == "f":
            with open(self.source.value, "r") as file:
                text = file.read()
        elif self.source.type == "view":
            text_report = self.repository.get_analyzed_text(self.source.value)
            print(text_report)
            return

        self.logger.info("Got the text")

        if text:
            self.logger.info("Started analyze the text")
            text_report = TextAnalyzer(text).report
            self.logger.info("Finished analyze the text")
            self.repository.add_analyzed_text(self.source.value, text_report)
            print("Stored analyzed text in DB")
        else:
            self.logger.error("There is no text")

    def load_text_from_url(self) -> Union[str, None]:
        try:
            res = requests.get(self.source.value)
            if res.status_code == 200:
                return res.text
            else:
                self.logger.error(
                    f"Response from server not successful: {res.status_code}"
                )
                return None
        except Exception as e:
            # Add more exactly exceptions
            self.logger.error(f"Failed to connect to server: {e}")
            return None

    @cached_property
    def logger(self) -> logging.Logger:
        logger = logging.getLogger(f"{self.source.value} Logger")
        logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler("textanalyzer.log")

        type_of_resource = {"f": "FILE", "r": "RESOURCE"}.get(
            self.source.type, "UNKNOWN"
        )
        file_handler.setFormatter(
            logging.Formatter(
                f"%(asctime)s|{type_of_resource}|{self.source.value}|%(message)s"
            )
        )
        logger.addHandler(file_handler)

        return logger
