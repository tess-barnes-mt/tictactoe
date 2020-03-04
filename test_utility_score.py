import unittest
import utility_score

class TestUtilityScore(unittest.TestCase):
    def setUp(self):
        self.utility_score = utility_score.UtilityScore()

    def test_utility_score_return_1_when_win_available(self):
        board = ['x', 'o', None, 'x', 'o', None, 'x', None, None]
        score = self.utility_score.get_score(board)
        self.assertEqual(score,1.0)

    def test_utility_score_returns_0_when_maximum_utility_zero(self):
        board = [None, None, None, None, None, None, None, None, None]
        score = self.utility_score.get_score(board)
        self.assertEqual(score, 0.0)

    def test_utility_score_returns_0_point_2_when_move_marks_two_in_one_triplet(self):
        boards = [
            ['o', None, None, None, None, 'o', None, 'x', 'x'],
            ['o', None, None, None, None, 'o', 'x', None, 'x'],
            ['o', None, None, None, None, 'o', 'x', 'x', None],
            [None, None, None, None, 'x', 'o', 'o', None, 'x'],
            [None, None, None, None, None, 'x', 'o', 'o', 'x'],
        ]
        for board in boards:
            score = self.utility_score.get_score(board)
            self.assertEqual(score, 0.2)

    def test_utility_score_returns_whether_game_is_won_based_on_board(self):
        winning_boards = [
            ['x','x','x','o','o'] + [None]*4,
            [None]* 3 + ['x','x','x','o','o', None],
            ['x', 'o', None, 'o', 'x', None, None, None, 'x'],
            [None, None, None, None, 'o', 'o', 'x', 'x', 'x'],
            [None, None, 'x', 'o', 'x', 'o', 'x', None, None],
            ['x', 'o', None, 'x', 'o', None, 'x', None, None],
            ['o', 'x', 'x', None, 'x', None, None, 'x', None],
            [None, 'o', 'x', None, 'o', 'x', None, None, 'x'],
        ]
        for board in winning_boards:
            game_is_won = self.utility_score.game_is_won(board)
            self.assertEqual(game_is_won, True)

# test utility scores for either player 