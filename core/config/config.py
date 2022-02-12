from ..singleton import Singleton


class Config(Singleton):
    def __init__(self):
        self.host = 'https://www.boredapi.com/api/activity?'
