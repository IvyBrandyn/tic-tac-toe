import random
from unittest import TestCase

from controllers.ai_player_controller import AIPlayerController
from controllers.game_controller import GameController
from controllers.grid_controller import GridController
from models.game import Game
from models.grid import Grid
from models.player import Player
from view.o_token import OToken
from view.x_token import XToken


class TestGameController(TestCase):
    def test_entire_game_with_two_AI(self):
        new_game = Game()
        new_game.game_mode = 2
        token_1 = XToken()
        token_2 = OToken()
        tokens = (token_1, token_2)
        new_game.add_token_options(tokens)

        game_controller = GameController()
        game_controller.assign_game(new_game)

        player_one = Player()
        player_two = Player()
        players = [player_one, player_two]
        game_controller.add_players_to_game(players)

        player_one_controller = AIPlayerController()
        player_two_controller = AIPlayerController()
        player_one_controller.assign_player(player_one)
        player_two_controller.assign_player(player_two)
        player_controllers = [player_one_controller, player_two_controller]

        player_one_controller.determine_name()
        player_two_controller.determine_name()

        random.shuffle(player_controllers)

        game_controller.assign_tokens(player_controllers)

        new_game.print_players()

        grid = Grid(3, 3)
        grid_controller = GridController()
        grid_controller.assign_grid(grid)
        while not new_game.game_over:
            game_controller.play_round(player_controllers, grid_controller)

    def test_horizontal_win(self):
        x_token = XToken()
        grid = Grid(3, 3)
        grid_controller = GridController()
        grid_controller.assign_grid(grid)
        grid.add_token_position(x_token, 0, 0)
        grid.add_token_position(x_token, 0, 1)
        grid.add_token_position(x_token, 0, 2)
        winner = grid_controller.check_for_win()
        assert winner == x_token

    def test_vertical_win(self):
        o_token = OToken()
        grid = Grid(3, 3)
        grid_controller = GridController()
        grid_controller.assign_grid(grid)
        grid.add_token_position(o_token, 0, 1)
        grid.add_token_position(o_token, 1, 1)
        grid.add_token_position(o_token, 2, 1)
        winner = grid_controller.check_for_win()
        assert winner == o_token

    def test_downward_diagonal_win(self):
        x_token = XToken()
        grid = Grid(3, 3)
        grid_controller = GridController()
        grid_controller.assign_grid(grid)
        grid.add_token_position(x_token, 0, 0)
        grid.add_token_position(x_token, 1, 1)
        grid.add_token_position(x_token, 2, 2)
        winner = grid_controller.check_for_win()
        assert winner == x_token

    def test_upward_diagonal_win(self):
        o_token = OToken()
        grid = Grid(3, 3)
        grid_controller = GridController()
        grid_controller.assign_grid(grid)
        grid.add_token_position(o_token, 0, 2)
        grid.add_token_position(o_token, 1, 1)
        grid.add_token_position(o_token, 2, 0)
        winner = grid_controller.check_for_win()
        assert winner == o_token

    def test_no_winner_board_full(self):
        x_token = XToken()
        o_token = OToken()
        grid = Grid(3, 3)
        grid_controller = GridController()
        grid_controller.assign_grid(grid)
        grid.add_token_position(x_token, 0, 0)
        grid.add_token_position(x_token, 0, 1)
        grid.add_token_position(x_token, 1, 2)
        grid.add_token_position(x_token, 2, 0)
        grid.add_token_position(x_token, 2, 1)
        grid.add_token_position(o_token, 0, 2)
        grid.add_token_position(o_token, 1, 0)
        grid.add_token_position(o_token, 1, 1)
        grid.add_token_position(o_token, 2, 2)
        winner = grid_controller.check_for_win()
        assert winner is None
        assert grid_controller.grid_is_full()
