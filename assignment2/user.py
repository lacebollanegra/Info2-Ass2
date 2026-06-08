################################################################################
# Author 1:      Simon Ehart
# MatNr 1:       12438518
# Author 2:      Florian Koeberl
# MatNr 2:       12403729
# Author 3:      Florian Faedler
# MatNr 3:       12422306
# File:          user.py
# Description:   Contains the user class.
# Comments:      nothing to add.
################################################################################

from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, user_id: int, name: str, email: str, birth_date: str, birth_place: str) -> None:
        self.id = user_id
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
