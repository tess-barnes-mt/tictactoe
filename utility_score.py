class UtilityScore():
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

    def get_score(self,board):
        for triplet in self.triplets:
            if board[triplet[0]] and board[triplet[0]] == board[triplet[1]] == board[triplet[2]]:
                return 1
            if board[triplet[0]] is None and board[triplet[1]] == 'x' and board[triplet[1]] == board[triplet[2]]:
                return 0.2
            if board[triplet[1]] is None and board[triplet[2]] == 'x' and board[triplet[0]] == board[triplet[2]]:
                return 0.2
            if board[triplet[2]] is None and board[triplet[0]] == 'x' and board[triplet[0]] == board[triplet[1]]: 
                return 0.2

        all_empty = True

        for position in board:
            if position != None:
                all_empty = False

        if all_empty:
            return 0.0
        
    def game_is_won(self,board):
        for triplet in self.triplets:
            if board[triplet[0]] and board[triplet[0]] == board[triplet[1]] == board[triplet[2]]:
                return True
        return False