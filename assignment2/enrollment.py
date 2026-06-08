################################################################################
# Author 1:      Simon Ehart
# MatNr 1:       01234567
# Author 2:      Flo 1
# MatNr 2:       12403729
# Author 3:      Florian Faedler
# MatNr 3:       12422306
# File:          grade.py
# Description:   Contains the Grade class
# Comments:      Linking a student to a course for a specific semester and managing their grades
################################################################################

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from student import Student
    from course import Course
    from grade import Grade

class Enrollment:
    total_enrollments: int = 0

    def __init__(self, student: Student, course: Course, semester: str):
        self.student = student
        self.course = course
        self.semester = semester
        self.grades: list[Grade] = []
        Enrollment.total_enrollments += 1

    @classmethod
    def enrollment_summary(cls) -> str:
        return f"Total number of enrollments: {cls.total_enrollments}"

    def __lshift__(self, grade: Grade) -> Enrollment:
        self.grades.append(grade)
        return self

    def __len__(self) -> int:
        return len(self.grades)

    def __call__(self, threshold: float) -> list[Grade]:
        return [g for g in self.grades if g.value >= threshold]