# receives board
# returns move

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

        if self.IsWon(board):
            return None

        # for triplet in triplets:
        available_options = []
        best_option = None
        best_utility_score = 0.0

        for triplet in self.triplets:
            for i in range(3):
                if board[triplet[i]] == None:
                    if triplet[i] not in available_options:
                        available_options.append(triplet[i])
        
        for option in available_options:
            trial_board = []
            trial_board.extend(board)
            trial_board[option] = 'x'
        
            if self.IsWon(trial_board):
                return option
            
            # know about related triplets
            # checking for high utility
            related = self.GetRelatedTriplets(option)
            score = 0.0
            for relation in related:
                score = self.GetUtilityScore(board, relation)

            if score > best_utility_score:
                best_utility_score = score
                best_option = option

        return best_option

    def GetRelatedTriplets(self,square):
        related = []
        for triplet in self.triplets:
            if square in triplet:
                related.append(triplet)
        return related

    def IsWon(self, board):
        for triplet in self.triplets:
            if board[triplet[0]] and board[triplet[0]] == board[triplet[1]] == board[triplet[2]]:
                return True
        return False

    def GetUtilityScore(self, board, relation):
        score = 0.0
        if board[relation[0]] is None and board[relation[1]] == 'o' and board[relation[1]] == board[relation[2]]:
            score = score + 0.2
        if board[relation[1]] is None and board[relation[2]] == 'o' and  board[relation[0]] == board[relation[2]]:
            score = score + 0.2
        if board[relation[2]] is None and board[relation[0]] == 'o' and  board[relation[0]] == board[relation[1]]:
            score = score + 0.2
        return score
