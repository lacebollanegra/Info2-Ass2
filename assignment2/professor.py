################################################################################
# Author 1:      Simon Ehart
# MatNr 1:       12438518
# Author 2:      Florian Koeberl
# MatNr 2:       12403729
# Author 3:      Florian Faedler
# MatNr 3:       12422306
# File:          professor.py
# Description:   Contains the Professor class.
# Comments:      nothing to add.
################################################################################

from assignment2.user import User


class Professor(User):
    def __init__(
        self,
        user_id: int,
        name: str,
        email: str,
        birth_date: str,
        birth_place: str,
        department: str,
        office: str,
    ) -> None:
        super().__init__(user_id, name, email, birth_date, birth_place)
        self.department = department
        self.office = office

    def get_email_signature(self) -> str:
        return f"Kind regards,\n{self.name}\n{10 * " - "}\nOffice {self.office}"

    @property
    def role(self) -> str:
        return "Professor"

    def info(self) -> str:
        line = "-" * 10
        return (
            f"Professor-Information:\n{line}\n"
            f"ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Email: {self.email}\n"
            f"Birthdate: {self.birth_date}\n"
            f"Birthplace: {self.birth_place}\n"
            f"Department: {self.department}\n"
            f"Office: {self.office}"
        )
