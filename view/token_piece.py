from abc import ABC, abstractmethod


class TokenPiece(ABC):
    @abstractmethod
    def draw_token(self, line: int) -> str:
        """Prints token piece"""
        raise NotImplementedError

    @abstractmethod
    def is_token(self, response: str):
        raise NotImplementedError
