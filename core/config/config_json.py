from ..singleton import Singleton


class ConfigJson(Singleton):
    def __init__(self):
        self.json = {"activity": "Cook something together with someone",
                     "type": "cooking", "participants": 2, "price": 0.3,
                     "link": "", "key": "1799120", "accessibility": 0.8}
