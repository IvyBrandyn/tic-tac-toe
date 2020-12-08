import random
from typing import List

from controllers.player_controller import PlayerController
from data import player_controller_data as data
from models.player import Player
from view.token_piece import TokenPiece


class AIPlayerController(PlayerController):
    def __init__(self):
        self.__player = None

    def select_row(self, rows: int):
        return self.select_row_or_column_base(data.SELECT_ROW_MESSAGE, rows)

    def select_column(self, columns: int):
        return self.select_row_or_column_base(data.SELECT_COLUMN_MESSAGE, columns)

    def select_row_or_column_base(self, selection_message, limit: int):
        selection = random.choice(range(0, limit))
        print(selection_message)
        print(selection)
        return selection

    def assign_player(self, player: Player):
        self.__player = player

    def determine_name(self):
        print(data.ENTER_PLAYER_NAME_MESSAGE)
        desired_name = random.choice(data.POSSIBLE_NAMES)
        print(desired_name)
        self.__player.name = desired_name

    def get_desired_token(self, token_options: List[TokenPiece]):
        print(self.__player.name + ": " + data.ENTER_PLAYER_TOKEN_MESSAGE)
        desired_token = random.choice(token_options)
        print(desired_token)
        new_token_options = token_options.copy()
        new_token_options.remove(desired_token)
        return desired_token, new_token_options

    def assign_token_to_player(self, token: TokenPiece):
        self.__player.token = token

    def print_player(self):
        print(self.__player)

    def retrieve_token(self):
        return self.__player.token
