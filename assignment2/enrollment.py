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

# Das verhindert zirkuläre Importe, da wir die Klassen nur für Type Hints brauchen
if TYPE_CHECKING:
    from assignment2.course import Course
    from assignment2.grade import Grade
    from assignment2.student import Student

class Enrollment:
    # Klassenattribut (Falle 2 gelöst: Zählt über alle Instanzen hinweg)
    total_enrollments: int = 0

    def __init__(self, student: Student, course: Course, semester: str) -> None:
        # Aggregation: student und course werden von außen übergeben
        self.student = student
        self.course = course
        self.semester = semester

        # Komposition: Die Liste wird zwingend HIER innen erstellt,
        # sie existiert nicht unabhängig vom Enrollment
        self.grades: list[Grade] = []

        # Klassenattribut bei jeder neuen Instanziierung erhöhen
        Enrollment.total_enrollments += 1

    @classmethod
    def enrollment_summary(cls) -> str:
        # Klassenmethode (Falle 3 gelöst)
        return f"Total number of enrollments: {cls.total_enrollments}"

    # --- Magic Methods ---

    def __lshift__(self, grade: Grade) -> Enrollment:
        """Fügt eine Note über den << Operator hinzu."""
        self.grades.append(grade)
        # return self ist Best Practice, damit man verketten kann:
        # enrollment << grade1 << grade2
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