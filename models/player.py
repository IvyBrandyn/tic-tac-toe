from view.token_piece import TokenPiece


class Player:
    def __init__(self):
        self.__name = "None"
        self.__score = 0
        self.__token = "None"

    def print_name(self):
        print(self.__name)

    @property
    def score(self) -> int:
        return self.__score

    @score.setter
    def score(self, new_score: int):
        self.__score = new_score

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name: str):
        self.__name = new_name

    @property
    def token(self) -> TokenPiece:
        return self.__token

    @token.setter
    def token(self, new_token):
        self.__token = new_token

    def __str__(self):
        return "Name: " + self.__name + " " * 5 + "Token: " + str(self.__token)
