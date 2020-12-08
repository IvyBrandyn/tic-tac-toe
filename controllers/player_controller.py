from abc import ABC, abstractmethod
from typing import List

from models.player import Player
from view.token_piece import TokenPiece


class PlayerController(ABC):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, "select_row")
            and hasattr(subclass, "select_column")
            and hasattr(subclass, "determine_name")
            and hasattr(subclass, "get_desired_token")
            and hasattr(subclass, "assign_token_to_player")
            and hasattr(subclass, "print_player")
            and hasattr(subclass, "retrieve_token")
        )

    @abstractmethod
    def select_row(self, rows: int):
        raise NotImplementedError

    @abstractmethod
    def select_column(self, columns: int):
        raise NotImplementedError

    @abstractmethod
    def assign_player(self, player: Player):
        raise NotImplementedError

    @abstractmethod
    def determine_name(self):
        raise NotImplementedError

    @abstractmethod
    def get_desired_token(self, token_options: List[TokenPiece]):
        raise NotImplementedError

    @abstractmethod
    def assign_token_to_player(self, token: TokenPiece):
        raise NotImplementedError

    @abstractmethod
    def print_player(self):
        raise NotImplementedError

    @abstractmethod
    def retrieve_token(self):
        raise NotImplementedError
