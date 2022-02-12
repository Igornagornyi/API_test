from __future__ import annotations


class Activity:
    def __init__(
            self,
            activity: str,
            type: str,
            participants: int,
            price: float,
            link: str,
            key: str,
            accessibility: float
    ) -> None:
        self.activity = activity
        self.type = type
        self.participants = participants
        self.price = price
        self.link = link
        self.key = key
        self.accessibility = accessibility

    @classmethod
    def from_response(cls, data: dict) -> Activity:
        return cls(**data)
