from core.config.config import Config
from core.singleton import Singleton

from requests import get

from activity_entities.activity import Activity


class ActivityService(Singleton):
    def __init__(self, config: Config) -> None:
        self.__config = config

    def from_response_activity(self) -> str:
        return Activity.from_response(
            get(url=f"{self.__config.host}participants=2").json()
        ).activity

    def from_response_type(self) -> str:
        return Activity.from_response(
            get(url=f"{self.__config.host}participants=2").json()
        ).type

    def from_response_price(self) -> float:
        return Activity.from_response(
            get(url=f"{self.__config.host}participants=2").json()
        ).price

    def from_response_participants(self) -> float:
        return Activity.from_response(
            get(url=f"{self.__config.host}participants=2").json()
        ).participants

    def from_response_link(self) -> str:
        return Activity.from_response(
            get(url=f"{self.__config.host}participants=2").json()
        ).link

    def from_response_key(self) -> str:
        return Activity.from_response(
            get(url=f"{self.__config.host}participants=2").json()
        ).key

    def from_response_accessibility(self) -> float:
        return Activity.from_response(
            get(url=f"{self.__config.host}participants=2").json()
        ).accessibility
