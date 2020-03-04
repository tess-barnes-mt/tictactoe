# receives board
# returns move

from utility_score import UtilityScore

class Algorythm():
    triplets = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    def GetMove(self,board):
        if len(board) != 9:
            raise Exception

        isEmpty = True
        for square in board:
            if square is not None:
                isEmpty = False
                break
        
        if isEmpty:
            return 0

        if UtilityScore().game_is_won(board):
            return None

        available_options = []
        moves_with_utility_scores = []

        for triplet in self.triplets:
            for i in range(3):
                if board[triplet[i]] == None:
                    if triplet[i] not in available_options:
                        available_options.append(triplet[i])
        
        for option in available_options:
            trial_board = []
            trial_board.extend(board)
            trial_board[option] = 'x'

            score = UtilityScore().get_score(trial_board)
            moves_with_utility_scores.append({ 'position': option, 'score': score })

        for potential_move in moves_with_utility_scores:
            if potential_move['score'] == 1.0:
                return potential_move['position']
                
