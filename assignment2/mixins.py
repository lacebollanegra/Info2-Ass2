################################################################################
# Author 1:      Simon Ehart
# MatNr 1:       12438518
# Author 2:      Florian Koeberl
# MatNr 2:       12403729
# Author 3:      Florian Faedler
# MatNr 3:       12422306
# File:          mixins.py
# Description:   Contains the required mixins.
# Comments:      nothing to add.
################################################################################


class ComparableMixin:
    _compare_key: str

    def _get_compare_value(self) -> object:
        return getattr(self, self._compare_key)

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self._get_compare_value() < other._get_compare_value()

    def __le__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self._get_compare_value() <= other._get_compare_value()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self._get_compare_value() == other._get_compare_value()


class ExportableMixin:
    def to_dict(self) -> dict[str, object]:
        return self.__dict__.copy()
