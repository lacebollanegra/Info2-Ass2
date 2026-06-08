################################################################################
# Author 1:      Simon Ehart
# MatNr 1:       01234567
# Author 2:      Flo 1
# MatNr 2:       12403729
# Author 3:      Florian Faedler
# MatNr 3:       12422306
# File:          grade.py
# Description:   Contains the Grade class
# Comments:      nothing to add
################################################################################

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from student import Student
    from enrollment import Enrollment


class GradeEvaluator:
    def __init__(self, threshold: float, passing_label: str = "Pass"):
        self.threshold = threshold
        self.passing_label = passing_label

    def __call__(self, enrollments: list[Enrollment]) -> list[Student]:
        student_grades: dict[Student, list[float]] = {}

        for enrollment in enrollments:
            if enrollment.student not in student_grades:
                student_grades[enrollment.student] = []
            for grade in enrollment.grades:
                student_grades[enrollment.student].append(grade.value)

        passing_students: list[Student] = []

        for student, grades in student_grades.items():
            if grades:
                average = sum(grades) / len(grades)
                if average >= self.threshold:
                    passing_students.append(student)

        return passing_students

    def __repr__(self) -> str:
        return f"GradeEvaluator(threshold={self.threshold}, passing_label='{self.passing_label}')"