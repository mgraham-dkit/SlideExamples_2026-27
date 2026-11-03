from types import NotImplementedType


class Game:
    _categories:list[str] = ["BOARD", "CARD", "CONSOLE", "PC"]
    _DEFAULT_NUM_PLAYERS = 2

    def __init__(self, name:str, num_players:int = _DEFAULT_NUM_PLAYERS, category:str = "BOARD"):
        self.name = name

        # Validate num_players and set to default if invalid information provided
        if num_players < 1:
            num_players = Game._DEFAULT_NUM_PLAYERS

        self.num_players = num_players

        # If no category is supplied
        if not category:
            category = Game._categories[0]
        else:
            category = category.upper()

        # If supplied category is invalid
        if category not in Game._categories:
            category = Game._categories[0]

        # Set game's official category
        self._category = category

    def __eq__(self, other: object) -> bool | NotImplementedType:
        if not isinstance(other, Game):
            return NotImplemented
        if self.name != other.name:
            return False
        if self.num_players != other.num_players:
            return False
        if self._category != other._category:
            return False
        return True

    def __ne__(self, other:object) -> bool | NotImplementedType:
        return not self == other

    def __hash__(self) -> int:
        return hash((self.name, self.num_players, self._category))

    def __str__(self) -> str:
        return f"{self.name}: A {self._category.lower()} game for {self.num_players} players."

    def __repr__(self) -> str:
        return f"Game[name={self.name}, num_players={self.num_players}, category={self._category}]"

    def __format__(self, format_spec:str) -> str:
        match format_spec.lower():
            case "simple":
                return f"{self.name} for {self.num_players} player(s)"
            case "file":
                return f"{self.name}%%{self.num_players}%%{self._category}"
            case _:
                return str(self)

    @staticmethod
    def add_category(new_category: str) -> bool:
        if not new_category:
            return False

        if new_category.upper() not in Game._categories:
            Game._categories.append(new_category.upper())
            return True
        return False
