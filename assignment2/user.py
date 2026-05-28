from abc import ABC, abstractmethod



class User(ABC):
    def __init__(self, id : int, name : str, email : str, birth_date : str, birth_place : str):
        self.id = id
        self.name = name
        self.email = email
        self.birth_date = birth_date
        self.birth_place = birth_place
    
    @property
    @abstractmethod
    def get_role(self) -> str:
        pass

    @abstractmethod
    def get_email_signature(self) -> str:
        pass

    def __repr__(self):
        return (f"User-Type: {self.get_role}, ID: {self.id}\nName: {self.name}\nEmail: {self.email}\nBirth date: {self.birth_date}\nBirth place: {self.birth_place}")
        
    


    

    