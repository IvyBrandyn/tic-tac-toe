from typing import List

from controllers.grid_controller import GridController
from controllers.player_controller import PlayerController
from data import game_controller_data as data
from models.game import Game
from models.player import Player


class GameController:
    def __init__(self):
        self.__game = None

    def play_round(
        self,
        player_controllers: List[PlayerController],
        grid_controller: GridController,
    ):
        for player_controller in player_controllers:
            row = None
            column = None
            while not grid_controller.check_if_position_available(row, column):
                grid_controller.print_grid_with_prompt()
                if self.game_won(player_controllers, grid_controller):
                    return
                if grid_controller.grid_is_full():
                    self.__game.game_over = True
                    return
                player_controller.print_player()
                rows, columns = grid_controller.get_grid_dimensions()
                row = player_controller.select_row(rows)
                column = player_controller.select_column(columns)
            player_token = player_controller.retrieve_token()
            grid_controller.place_token_in_spot(player_token, row, column)

    def game_won(
        self,
        player_controllers: List[PlayerController],
        grid_controller: GridController,
    ) -> bool:
        winning_token = grid_controller.check_for_win()
        if winning_token is not None:
            for player_controller in player_controllers:
                if player_controller.retrieve_token() == winning_token:
                    player_controller.print_player()
                    print(data.WINNING_MESSAGE)
                    self.__game.game_over = True
                    return True
        else:
            return False

    def show_prompt(self):
        print(data.PROMPT_MESSAGE)

    def determine_game_mode(self):
        user_response = 0
        while user_response not in range(1, 3):
            try:
                user_response = int(input(data.ENTER_PLAYERS_MESSAGE))
            except ValueError:
                print(data.ENTER_PLAYERS_VALUE_ERROR_MESSAGE)
        self.__game.game_mode = user_response

    def assign_game(self, new_game: Game):
        self.__game = new_game

    def add_players_to_game(self, players: List[Player]):
        for player in players:
            self.__game.add_player(player)

    def assign_tokens(self, player_controllers: List[PlayerController]):
        if len(player_controllers) == 2:
            player_making_choice = player_controllers[0]
            other_player = player_controllers[1]
        else:
            #   Implement token assign for > 2 players ?
            pass
        chosen_token, tokens_left = player_making_choice.get_desired_token(
            self.__game.token_options
        )
        if len(tokens_left) == 1:
            player_making_choice.assign_token_to_player(chosen_token)
            other_player.assign_token_to_player(tokens_left[0])
        else:
            #   Finish implementing assigning for > 2 players
            chosen_token, tokens_left = other_player.get_desired_token(tokens_left)
            other_player.assign_token_to_player(chosen_token)
