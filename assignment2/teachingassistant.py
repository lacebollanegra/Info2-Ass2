################################################################################
# Author 1:      Simon Ehart
# MatNr 1:       12438518
# Author 2:      Florian Koeberl
# MatNr 2:       12403729
# Author 3:      Florian Faedler
# MatNr 3:       12422306
# File:          teachingassistant.py
# Description:   Contains the teachingAssistant class.
# Comments:      nothing to add.
################################################################################

from assignment2.course import Course
from assignment2.professor import Professor
from assignment2.student import Student
from assignment2.user import User


class TeachingAssistant(Student, Professor):
    def __init__(
            self,
            user_id: int,
            name: str,
            email: str,
            birth_date: str,
            birth_place: str,
            matriculation_id: int,
            program: str,
            department: str,
            office: str,
            supervised_course: Course,
    ) -> None:
        User.__init__(self, user_id, name, email, birth_date, birth_place)

        self.matriculation_id = matriculation_id
        self.program = program
        self.department = department
        self.office = office
        self.supervised_course = supervised_course

    @property
    def role(self) -> str:
        return "Teaching Assistant"

    def get_email_signature(self) -> str:
        return f"Best regards,\n{self.name}\nTeaching Assistant for {self.supervised_course.name}"

    def info(self) -> str:
        return (
            "Teaching Assistant Information:\n"
            f"ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Email: {self.email}\n"
            f"Birth date: {self.birth_date}\n"
            f"Birth place: {self.birth_place}\n"
            f"Matriculation ID: {self.matriculation_id}\n"
            f"Program: {self.program}\n"
            f"Department: {self.department}\n"
            f"Office: {self.office}\n"
            f"Supervised course: {self.supervised_course.info()}"
        )

