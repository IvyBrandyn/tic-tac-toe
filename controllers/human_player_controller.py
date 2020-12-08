from typing import List

from controllers.player_controller import PlayerController
from data import player_controller_data as data
from models.player import Player
from view.token_piece import TokenPiece


class HumanPlayerController(PlayerController):
    def __init__(self):
        self.__player = None

    def select_row(self, rows: int):
        return self.select_row_or_column_base(data.SELECT_ROW_MESSAGE, rows)

    def select_column(self, columns: int):
        return self.select_row_or_column_base(data.SELECT_COLUMN_MESSAGE, columns)

    def select_row_or_column_base(self, selection_message, limit: int):
        selection = -1
        while selection not in range(0, limit):
            if selection != -1:
                print(data.OUT_OF_RANGE_MESSAGE)
            try:
                selection = int(input(selection_message))
            except ValueError:
                print(data.SELECT_ROW_OR_COLUMN_ERROR)
        return selection

    def assign_player(self, player: Player):
        self.__player = player

    def determine_name(self):
        desired_name = ""
        while len(desired_name) == 0:
            desired_name = input(data.ENTER_PLAYER_NAME_MESSAGE + "\n")
        self.__player.name = desired_name

    def get_desired_token(self, token_options: List[TokenPiece]):
        while True:
            desired_token = input(
                self.__player.name + ": " + data.ENTER_PLAYER_TOKEN_MESSAGE + "\n"
            )
            for token in token_options:
                if token.is_token(desired_token):
                    desired_token = token
                    new_token_options = token_options.copy()
                    new_token_options.remove(desired_token)
                    return desired_token, new_token_options

    def assign_token_to_player(self, token: TokenPiece):
        self.__player.token = token

    def print_player(self):
        print(self.__player)

    def retrieve_token(self):
        return self.__player.token
