from types import NotImplementedType


class Customer:
    def __init__(self, name: str):
        self._name = name

    def get_name(self) -> str:
        return self._name

    def __str__(self) -> str:
        return f"Customer(_name={self._name})"

    def __eq__(self, other: object) -> NotImplementedType | bool:
        if not isinstance(other, Customer):
            return NotImplemented

        return self._name.lower() == other._name.lower()

    def __hash__(self) -> int:
        return hash(self._name.lower())