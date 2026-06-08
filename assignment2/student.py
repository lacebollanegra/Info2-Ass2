################################################################################
# Author 1:      Simon Ehart
# MatNr 1:       12438518
# Author 2:      Florian Koeberl
# MatNr 2:       12403729
# Author 3:      Florian Faedler
# MatNr 3:       12422306
# File:          student.py
# Description:   Contains the Student class.
# Comments:      nothing to add.
################################################################################

from assignment2.user import User
from assignment2.errors import NumberNotSuitableError
from assignment2.mixins import ComparableMixin

class Student(ComparableMixin, User):
    _compare_key = "name"

    def __init__(
        self,
        user_id: int,
        name: str,
        email: str,
        birth_date: str,
        birth_place: str,
        matriculation_id: int,
        program: str,
    ) -> None:
        super().__init__(user_id, name, email, birth_date, birth_place)
        self.matriculation_id = matriculation_id
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
        line = "-" * 10
        signature = f"Yours sincerely,\n{self.name}\n{line}"
        return signature

    @property
    def role(self) -> str:
        return "Student"

    def info(self) -> str:
        line = "-" * 10
        return (
            f"Student-Information:\n{line}\n"
            f"ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Email: {self.email}\n"
            f"Birthdate: {self.birth_date}\n"
            f"Birthplace: {self.birth_place}\n"
            f"Matriculation-ID: {self.matriculation_id}\n"
            f"Program: {self.program}"
        )