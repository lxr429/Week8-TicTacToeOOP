import unittest
import logic


class TestLogic(unittest.TestCase):

    def test_initialize_empty_board(self):
        # Test that the game is initialized with an empty board
        board = logic.make_empty_board()
        self.assertEqual(board, [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ])

    def test_initialize_game_with_two_players(self):
        # Test that the game is initialized with 2 players (human-human)
        game = logic.Game(player_mode='human-human')
        self.assertEqual(len(game.players), 2)

    def test_initialize_game_with_one_player(self):
        # Test that the game is initialized with 1 player (human-bot)
        game = logic.Game(player_mode='human-bot')
        self.assertEqual(len(game.players), 1)

    def test_assign_unique_pieces(self):
        # Test that players are assigned unique pieces (X or O)
        game = logic.Game(player_mode='human-human')
        self.assertNotEqual(game.players[0].piece, game.players[1].piece)

    def test_alternate_turns(self):
        # Test that after one player plays, the other player has a turn
        game = logic.Game(player_mode='human-human')
        initial_turn = game.current_player
        game.play(0, 0)  # Assuming (0, 0) is a valid move
        self.assertNotEqual(initial_turn, game.current_player)

    def test_detect_winner_X_wins(self):
        # Test that the correct game winner (if one exists) is detected
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')

    def test_detect_winner_Draw(self):
        # Test that draw games are identified
        board = [
            ['X', 'O', 'X'],
            ['X', 'O', 'O'],
            ['O', 'X', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'Draw')

    def test_players_can_play_in_viable_spots(self):
        # Test that players can play only in viable spots
        game = logic.Game(player_mode='human-human')
        self.assertTrue(game.is_valid_move(0, 0))  # Assuming (0, 0) is a valid move
        self.assertFalse(game.is_valid_move(0, 0))  # Assuming (0, 0) is already taken

    def test_detect_winner_no_winner(self):
        # Test that all winning end of the games detected
        board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X', 'O'],
        ]
        self.assertIsNone(logic.get_winner(board))


if __name__ == '__main__':
    unittest.main()
