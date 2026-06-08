################################################################################
# Author 1:      Simon Ehart
# MatNr 1:       12438518
# Author 2:      Florian Koeberl
# MatNr 2:       12403729
# Author 3:      Florian Faedler
# MatNr 3:       12422306
# File:          enrollment.py
# Description:   Contains the enrollment class.
# Comments:      nothing to add.
################################################################################

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from course import Course
    from grade import Grade
    from student import Student


class Enrollment:
    total_enrollments: int = 0

    def __init__(self, student: Student, course: Course, semester: str) -> None:
        self.student = student
        self.course = course
        self.semester = semester

        self.grades: list[Grade] = []

        Enrollment.total_enrollments += 1

    @classmethod
    def enrollment_summary(cls) -> str:
        return f"Total number of enrollments: {cls.total_enrollments}"

    def __lshift__(self, grade: Grade) -> Enrollment:
        """Fügt eine Note über den << Operator hinzu."""
        self.grades.append(grade)

        return self

    def __len__(self) -> int:
        """Gibt die Anzahl der gespeicherten Noten zurück."""
        return len(self.grades)

    def __call__(self, threshold: float) -> list[Grade]:
        """
        Macht das Objekt aufrufbar. Gibt alle Noten zurück,
        die größer oder gleich dem threshold sind.
        """
        return [g for g in self.grades if g.value >= threshold]

    def __repr__(self) -> str:
        return (
            f"Enrollment(student={self.student.name!r}, "
            f"course={self.course.name!r}, "
            f"semester={self.semester!r}, "
            f"grades={self.grades!r})"
        )
