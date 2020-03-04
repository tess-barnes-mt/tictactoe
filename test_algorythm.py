import unittest
import algorythm

class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.board = [None] * 9

    def test_when_algorythm_receives_empty_board_returns_move(self):
        tictac = algorythm.Algorythm()
        self.assertEqual(tictac.GetMove(self.board), 0)

    # def test_when_algorythm_receives_first_board_returns_move(self):
    #     tictac = algorythm.Algorythm()
    #     board = [None]*4 + ['o'] + [None]*4
    #     self.assertEqual(tictac.GetMove(board), 0)

    def test_when_create_algorythm_fails_if_not_9_items(self):
        tictac = algorythm.Algorythm()
        with self.assertRaises(Exception):
            tictac.GetMove([])

    def test_algorythm_does_not_return_taken_move(self):
        self.board[0] = 'x'
        tictac = algorythm.Algorythm()
        self.assertNotEqual(tictac.GetMove(self.board), 0)

    def test_algorythm_ends_game_on_full(self):
        self.board = ['x','o','x','o','x','o','x','o','x']
        tictac = algorythm.Algorythm()
        self.assertEqual(None, tictac.GetMove(self.board))

    def test_algorythm_ends_game_on_win(self):
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
        tictac = algorythm.Algorythm()
        for board in winning_boards:
            self.assertEqual(None, tictac.GetMove(board))
    
    def test_algorythm_does_not_return_first_available(self):
        self.board = ['x', 'o', None, 'x', 'o', None, None, None, None]
        tictac = algorythm.Algorythm()
        self.assertNotEqual(tictac.GetMove(self.board), 2)

    def test_algorythm_wins_as_x(self):
        self.board = ['x', 'o', None, 'x', 'o', None, None, None, None]
        tictac = algorythm.Algorythm()
        self.assertEqual(tictac.GetMove(self.board), 6)

    def test_plays_a_defensive_move(self):
        self.board = [None, 'o', 'x',None,'o']+[None]*4
        tictac = algorythm.Algorythm()
        self.assertEqual(tictac.GetMove(self.board), 7)
