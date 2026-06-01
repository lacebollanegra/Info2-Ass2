from assignment2.user import User
from assignment2.errors import NumberNotSuitableError

class Student(User):
    
    def __init__(
    self,
    id: int,
    name: str,
    email: str,
    birth_date: str,
    birth_place: str,
    matriculation_id: int,
    program: str,
    ) -> None:
        super().__init__(id,name, email, birth_date, birth_place)
        self._matriculation_id = matriculation_id
        self.program = program

    @property
    def matriculation_id(self) -> int:
        return self._matriculation_id

    @matriculation_id.setter
    def matriculation_id(self, matriculation_id: int) -> None:
        if matriculation_id < 0 or len(str(matriculation_id)) != 8:
            raise NumberNotSuitableError("Matriculation-ID must be a positive number of 8 digits.")
        self._matriculation_id = matriculation_id

    def get_email_signature(self) -> str:
        signature = f"Yours sincerely,\n {self.name}\n{10* "-"}"
        return signature

    @property
    def role(self) -> str:
        return "Student"
    
    def info(self) -> str:
        return f"Student-Information:\n{10*"-"}\nID: {self.id}\nName: {self.name}\n Email: {self.email}\n Birthdate: {self.birth_date}\nBirthplace: {self.birth_place}\nMatriculation-ID: {self.matriculation_id}\nProgram: {self.program}"
    





