from board import Board
import math

class mainPlayer:
    def __init__(self, max_depth):
        self.max_depth = max_depth

    # Assign integer scores to the three terminal states of the game.
    # P2_WIN_SCORE < TIE_SCORE < P1_WIN_SCORE
    P1_WIN_SCORE = 100
    P2_WIN_SCORE = -100
    TIE_SCORE = 0

    def heuristic(self, board):
        if board.game_over:
            score = (
                self.P1_WIN_SCORE
                if board.winner == 0
                else self.P2_WIN_SCORE
                if board.winner == 1
                else self.TIE_SCORE
            )
            return score
        else:
            return board.p1_pot - board.p2_pot

    def findMove(self, trace):
        board = Board(trace)
        options = list(board.getAllValidMoves())
        best_move = options[0]
        bestScore = -math.inf
        for move in options:
            board.makeMove(move)
            score = self.heuristic(board)
            if score > bestScore:
                best_move = move
                bestScore = score
        return best_move


class manual(mainPlayer):
    def __init__(self, max_depth=None):
        mainPlayer.__init__(self, max_depth)

    def findMove(self, trace):
        board = Board(trace)
        opts = "  "
        for c in range(6):
            opts += " " + (str(c + 1) if board.isValidMove(c) else " ") + "  "

        while True:
            if board.turn == 0:
                print("\n")
                board.printSpaced()
                print(opts)
                pit = input("Pick a pit (P1 side): ")
            else:
                print("\n")
                print(" " + opts[::-1])
                board.printSpaced()
                pit = input("Pick a pit (P2 side): ")
            try:
                pit = int(pit) - 1
            except ValueError:
                continue
            if board.isValidMove(pit):
                return pit


class random(mainPlayer):
    def __init__(self, max_depth=None):
        mainPlayer.__init__(self, max_depth)
        self.random = random.Random(13487951347859)

    def findMove(self, trace):
        board = Board(trace)
        options = list(board.getAllValidMoves())
        return self.random.choice(options)

class PlayerMM(mainPlayer):
    def minimax(self, board, depth):
        if depth == 0 or board.game_over:
            return None, self.heuristic(board)
        if board.turn == 0:
            bestScore = -math.inf
            bestMove = None
            for move in board.getAllValidMoves():
                board.makeMove(move)
                _, score = self.minimax(board, depth - 1)
                board.undoMove()
                if score > bestScore:
                    bestScore = score
                    bestMove = move
            return (bestMove, bestScore)
        else:
            bestScore = math.inf
            bestMove = None
            for move in board.getAllValidMoves():
                board.makeMove(move)
                _, score = self.minimax(board, depth - 1)
                board.undoMove()
                if score < bestScore:
                    bestScore = score
                    bestMove = move
            return (bestMove, bestScore)

    def findMove(self, trace):
        board = Board(trace)
        move, score = self.minimax(board, self.max_depth)
        return move


class PlayerAB(mainPlayer):
    def alphaBeta(self, board, depth, alpha, beta):
        alpha = -math.inf
        beta = math.inf
        if depth == 0 or board.game_over:
            return None, self.heuristic(board)
        if board.turn == 0:
            bestScore = -math.inf
            bestMove = None
            for move in board.getAllValidMoves():
                board.makeMove(move)
                _, score = self.alphaBeta(board, depth - 1, alpha, beta)
                board.undoMove()
                if score > bestScore:
                    bestScore = score
                    bestMove = move
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
            return (bestMove, bestScore)
        else:
            bestScore = math.inf
            bestMove = None
            for move in board.getAllValidMoves():
                board.makeMove(move)
                _, score = self.alphaBeta(board, depth - 1, alpha, beta)
                board.undoMove()
                if score < bestScore:
                    bestScore = score
                    bestMove = move
                beta = min(beta, score)
                if beta <= alpha:
                    break
            return (bestMove, bestScore)

        raise NotImplementedError

    def findMove(self, trace):
        board = Board(trace)
        move, score = self.alphaBeta(board, self.max_depth, -math.inf, math.inf)
        return move


class PlayerDP(PlayerAB):
    def __init__(self, max_depth):
        PlayerAB.__init__(self, max_depth)
        self.resolved = {}
    def heuristic(self, board):
        if board.state in self.resolved:
            return self.resolved[board.state]
        else:
            score = super().heuristic(board)
            self.resolved[board.state] = score
            return score

# This will inherit findMove from above, but will override the heuristic function with
# a new one; it can swap out the type of player by changing X in "class TestPlayer(X):"
class TestPlayer(mainPlayer):
    def heuristic(self):
        score = 0
        if board.game_over:
            score = (
                self.P1_WIN_SCORE
                if board.winner == 0
                else self.P2_WIN_SCORE
                if board.winner == 1
                else self.TIE_SCORE
            )
        else:
            score = board.p1_pot - board.p2_pot
        return score
