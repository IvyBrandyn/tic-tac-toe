import random

from controllers.ai_player_controller import AIPlayerController
from controllers.game_controller import GameController
from controllers.grid_controller import GridController
from controllers.human_player_controller import HumanPlayerController
from data import main_data as data
from models.game import Game
from models.grid import Grid
from models.player import Player
from view.o_token import OToken
from view.x_token import XToken

if __name__ == "__main__":
    while True:
        new_game = Game()

        token_1 = XToken()
        token_2 = OToken()
        tokens = (token_1, token_2)
        new_game.add_token_options(tokens)

        game_controller = GameController()
        game_controller.assign_game(new_game)

        game_controller.show_prompt()
        game_controller.determine_game_mode()

        player_one = Player()
        player_two = Player()
        players = [player_one, player_two]
        game_controller.add_players_to_game(players)

        player_one_controller = None
        player_two_controller = None
        if new_game.is_single_player():
            player_one_controller = HumanPlayerController()
            player_two_controller = AIPlayerController()
        else:
            player_one_controller = HumanPlayerController()
            player_two_controller = HumanPlayerController()
        player_one_controller.assign_player(player_one)
        player_two_controller.assign_player(player_two)
        player_controllers = [player_one_controller, player_two_controller]

        print(data.PLAYER_ONE_FIRST_MESSAGE)
        player_one_controller.determine_name()
        print(data.PLAYER_TWO_NEXT_MESSAGE)
        player_two_controller.determine_name()

        print(data.RANDOMLY_SELECT_FIRST_PLAYER)
        random.shuffle(player_controllers)

        game_controller.assign_tokens(player_controllers)

        new_game.print_players()

        grid = Grid(data.GRID_ROWS, data.GRID_COLUMNS)
        grid_controller = GridController()
        grid_controller.assign_grid(grid)

        while not new_game.game_over:
            game_controller.play_round(player_controllers, grid_controller)

        play_again = input(data.PLAY_AGAIN_MESSAGE)
        if str.lower(play_again) not in ["yes", "y"]:
            break
