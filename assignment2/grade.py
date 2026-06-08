################################################################################
# Author 1:      Simon Ehart
# MatNr 1:       12438518
# Author 2:      Flo 1
# MatNr 2:       12403729
# Author 3:      Florian Faedler
# MatNr 3:       12422306
# File:          grade.py
# Description:   Contains the Grade class.
# Comments:      nothing to add.
################################################################################

from __future__ import annotations

from datetime import date


class Grade:
    def __init__(self, grade_type: str, value: float, grade_date: date, retry: int) -> None:
        self.type = grade_type
        self.value = value
        self.date = grade_date
        self.retry = retry

    def __add__(self, other: Grade) -> Grade:
        average_value = (self.value + other.value) / 2
        return Grade("Average", average_value, self.date, self.retry)

    def __mul__(self, factor: float) -> Grade:
        scaled_value = self.value * factor
        return Grade(self.type, scaled_value, self.date, self.retry)

    def __lt__(self, other: Grade) -> bool:
        return self.value < other.value

    def __le__(self, other: Grade) -> bool:
        return self.value <= other.value

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Grade):
            return False
        return self.type == other.type and self.value == other.value

    def __repr__(self) -> str:
        return f"Grade(type={self.type!r}, value={self.value!r}, " f"date={self.date!r}, retry={self.retry!r})"
