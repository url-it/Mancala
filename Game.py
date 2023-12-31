from board import Board
from player import *
import sys

class Game:
    def __init__(self, trace, player1, player2):
        self.trace = trace
        self.player1 = player1
        self.player2 = player2

    def runGame(self):
        board = Board(self.trace)
        while not board.game_over:
            if board.turn == 0:
                if not isinstance(self.player1, manual):
                    print("Player 1 is thinking")

                move = self.player1.findMove(board.trace)
            else:
                if not isinstance(self.player2, manual):
                    print("Player 2 is thinking")
                move = self.player2.findMove(board.trace)
            board.makeMove(move)
            board.print()
        if board.winner == -1:
            print("It is a draw!")
        elif board.winner == 0:
            print("Player 1 wins!")
        elif board.winner == 1:
            print("Player 2 wins!")


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        trace = sys.argv[1]
    else:
        trace = ""
    # Types of players:
    #  manual() - human player
    #  PlayerMM(max_depth) - minimax player with max_depth search
    #  PlayerAB(max_depth) - alpha-beta player with max_depth search
    #  random() - random player
    #  TestPlayer() - player that always chooses the first valid move

    p1 = PlayerAB(1)
    p2 = PlayerMM(2)
    g = Game(trace, p1, p2)

    g.runGame()
