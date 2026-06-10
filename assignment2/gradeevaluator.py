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
from assignment2.grade import Grade
from assignment2.student import Student


class GradeEvaluator:
    def __init__(self, threshold: float, passing_label: str = "Pass") -> None:
        self.threshold = threshold
        self.passing_label = passing_label

    def __call__(self, enrollments: list[Enrollment]) -> list[Student]:
        students_by_id: dict[int, Student] = {}
        grades_by_student_id: dict[int, list[Grade]] = {}

        for enrollment in enrollments:
            student_id = enrollment.student.matriculation_id

            students_by_id[student_id] = enrollment.student

            if student_id not in grades_by_student_id:
                grades_by_student_id[student_id] = []

            grades_by_student_id[student_id].extend(enrollment.grades)

        passing_students: list[Student] = []

        for student_id, grades in grades_by_student_id.items():
            if len(grades) == 0:
                continue

            average = sum(grade.value for grade in grades) / len(grades)

            if average >= self.threshold:
                passing_students.append(students_by_id[student_id])

        return passing_students

    def __repr__(self) -> str:
        return f"GradeEvaluator(threshold={self.threshold}, passing_label={self.passing_label!r})"
