################################################################################
# Author 1:      Simon Ehart
# MatNr 1:       12438518
# Author 2:      Flo 1
# MatNr 2:       12403729
# Author 3:      Flo 2
# MatNr 3:       01234567
# File:          course.py
# Description:   Contains the Course dataclass.
# Comments:      nothing to add.
################################################################################

from dataclasses import dataclass


@dataclass
class Course:
    code: str
    name: str
    ects: int
    lang: str

    def info(self) -> str:
        return f"{self.code}: {self.name} ({self.ects} ECTS, {self.lang})"