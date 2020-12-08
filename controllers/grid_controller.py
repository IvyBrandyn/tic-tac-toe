import numpy as np

from models.grid import Grid
from view.token_piece import TokenPiece


class GridController:
    def __init__(self):
        self.__grid = None

    def assign_grid(self, grid: Grid):
        self.__grid = grid

    def print_grid_with_prompt(self):
        print(self.__grid)

    def check_if_position_available(self, row: int, column: int):
        return self.__grid.check_if_position_available(row, column)

    def grid_is_full(self):
        return self.__grid.is_full()

    def place_token_in_spot(self, token: TokenPiece, row: int, column: int):
        self.__grid.add_token_position(token, row, column)

    def check_for_win(self):
        winner_token_row = self.check_for_win_rows(self.__grid.token_positions)
        winner_token_column = self.check_for_win_rows(
            np.transpose(self.__grid.token_positions).tolist()
        )
        winner_token_diag = self.check_diagonals_for_win(self.__grid.token_positions)
        winner_token_rev_diag = self.check_diagonals_for_win(
            np.fliplr(self.__grid.token_positions).tolist()
        )
        winner_token_options = [
            winner_token_row,
            winner_token_column,
            winner_token_diag,
            winner_token_rev_diag,
        ]
        for winning_possibility in winner_token_options:
            if winning_possibility is not None:
                return winning_possibility
        return None

    def check_for_win_rows(self, token_positions: list):
        for row in token_positions:
            if len(set(row)) == 1 and row[0] is not None:
                return row[0]
        return None

    def check_diagonals_for_win(self, token_positions: list):
        if len(set(np.diagonal(token_positions))) == 1:
            return np.diagonal(token_positions)[0]
        return None

    def get_grid_dimensions(self):
        return self.__grid.rows, self.__grid.columns
