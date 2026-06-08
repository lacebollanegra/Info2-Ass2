################################################################################
# Author 1:      Simon Ehart
# MatNr 1:       12438518
# Author 2:      Florian Koeberl
# MatNr 2:       12403729
# Author 3:      Florian Faedler
# MatNr 3:       12422306
# File:          gradeevaluator.py
# Description:   Contains the gradeEvaluator class.
# Comments:      nothing to add.
################################################################################

from assignment2.enrollment import Enrollment
from assignment2.student import Student


class GradeEvaluator:
    def __init__(self, threshold: float, passing_label: str = "Pass") -> None:
        self.threshold = threshold
        self.passing_label = passing_label

    def __call__(self, enrollments: list[Enrollment]) -> list[Student]:
        passing_students: list[Student] = []

        for enrollment in enrollments:
            if len(enrollment.grades) == 0:
                continue

            total = 0.0
            for grade in enrollment.grades:
                total += grade.value

            average = total / len(enrollment.grades)

            if average >= self.threshold and enrollment.student not in passing_students:
                passing_students.append(enrollment.student)

        return passing_students

    def __repr__(self) -> str:
        return f"GradeEvaluator(threshold={self.threshold}, passing_label={self.passing_label!r})"