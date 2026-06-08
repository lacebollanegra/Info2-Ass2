################################################################################
# Author 1:      Simon Ehart
# MatNr 1:       12438518
# Author 2:      Florian Koeberl
# MatNr 2:       12403729
# Author 3:      Florian Faedler
# MatNr 3:       12422306
# File:          course.py
# Description:   Contains the course dataclass.
# Comments:      nothing to add.
################################################################################

from dataclasses import dataclass

from assignment2.mixins import ExportableMixin


@dataclass
class Course(ExportableMixin):
    code: str
    name: str
    ects: int
    lang: str

    def info(self) -> str:
        return f"{self.code}: {self.name} ({self.ects} ECTS, {self.lang})"
