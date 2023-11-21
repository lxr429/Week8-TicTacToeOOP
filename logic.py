# logic.py

class TicTacToe:
    def __init__(self):
        self.board = self.make_empty_board()
        self.winner = None

    @staticmethod
    def make_empty_board():
        return [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

    def get_winner(self):
        for n in range(3):
            if self.board[n][0] == self.board[n][1] == self.board[n][2] and self.board[n][0] is not None:
                return self.board[n][0]
            if self.board[0][n] == self.board[1][n] == self.board[2][n] and self.board[0][n] is not None:
                return self.board[0][n]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] is not None:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] is not None:
            return self.board[0][2]
        if all(self.board[i][j] is not None for i in range(3) for j in range(3)):
            return 'Draw'

    def other_player(self, player):
        return 'O' if player == 'X' else 'X'

    def print_board(self):
        for row in self.board:
            print(" | ".join(cell if cell is not None else " " for cell in row))
            print("-" * 9)