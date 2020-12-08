from typing import Tuple

from models.player import Player
from view.token_piece import TokenPiece


class Game:
    def __init__(self):
        self.__number_players = 0
        self.__players = []
        self.__game_mode = 0
        self.__game_over = False
        self.__token_options = []

    def add_player(self, new_player: Player):
        self.__players.append(new_player)
        self.__number_players += 1

    def print_players(self):
        for player in self.__players:
            print(player)

    def is_single_player(self):
        return self.__game_mode == 1

    def add_token_options(self, tokens: Tuple[TokenPiece]):
        for token in tokens:
            self.__token_options.append(token)

    @property
    def token_options(self):
        return self.__token_options

    @property
    def number_players(self):
        return self.__number_players

    @property
    def players(self):
        return self.__players

    @property
    def game_mode(self):
        return self.__game_mode

    @game_mode.setter
    def game_mode(self, select_mode):
        self.__game_mode = select_mode

    @property
    def game_over(self):
        return self.__game_over

    @game_over.setter
    def game_over(self, update: bool):
        self.__game_over = update
