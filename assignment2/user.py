from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, id: int, name: str, email: str, birth_date: str, birth_place: str) -> None:
        self.id = id
        self.name = name
        self.email = email
        self.birth_date = birth_date
        self.birth_place = birth_place

    @property
    @abstractmethod
    def role(self) -> str:
        pass

    @abstractmethod
    def get_email_signature(self) -> str:
        pass

    def __repr__(self) -> str:
        return f"User-Type: {self.role}, ID: {self.id}\nName: {self.name}\nEmail: {self.email}\nBirth date: {self.birth_date}\nBirth place: {self.birth_place}"
