class Board:
    def __init__(self, trace=None):
        self.board_history = []
        self.board = [4,4,4,4,4,4,0,4,4,4,4,4,4,0,0]
        self._trace = []
        self.game_over = False
        if not (trace is None):
            for c in trace:
                if not self.isValidMove(int(c)):
                    print('Warning: invalid move skipped.')
                    continue
                self.makeMove(int(c))

    @property
    def p1_pits(self):
        return self.board[0:6]

    @property
    def p1_pot(self):
        return self.board[6]

    @property
    def p2_pits(self):
        return self.board[7:13]

    @property
    def p2_pot(self):
        return self.board[13]

    @property
    def turn(self):
        return self.board[14]

    @turn.setter
    def turn(self, value):
        self.board[14] = value

    @property
    def winner(self):
        if not self.game_over:
            return None
        if self.p1_pot > self.p2_pot:
            return 0
        if self.p2_pot > self.p1_pot:
            return 1
        return -1

    def isValidMove(self, pit):
        if self.game_over:
            return False
        if pit < 0 or pit > 5:
            return False
        if self.turn == 0:
            return self.board[pit] > 0
        return self.board[7+pit] > 0

    def makeMove(self, move):
        self._trace.append(move)
        self.board_history.append(self.board[:])

        player = self.turn
        pit = player*7 + move

        stones = self.board[pit]
        self.board[pit] = 0

        while stones > 0:
            if (pit == 5 and player == 1) or (pit == 12 and player == 0):
                pit += 2
            else:
                pit += 1
            pit %= 14
            self.board[pit] += 1
            stones -= 1
        if pit != 6 and pit != 13:
            self.turn = 1 - self.turn
            side = pit // 7
            across_pit = 12 - pit
            if side == player and self.board[pit] == 1 and self.board[across_pit] != 0:
                player_pot = 7*player+6
                self.board[player_pot] += 1 + self.board[across_pit]
                self.board[pit] = 0
                self.board[across_pit] = 0

        p1_total = sum(self.board[0:6])
        p2_total = sum(self.board[7:13])

        if p1_total == 0 or p2_total == 0 :
            self.board[6] += p1_total
            self.board[13] += p2_total
            self.board[0:6] = [0, 0, 0, 0, 0, 0]
            self.board[7:13] = [0, 0, 0, 0, 0, 0]
            self.game_over = True

    def undoMove(self):
        self.board = self.board_history.pop()
        self._trace.pop()
        self.game_over = False

    def getAllValidMoves(self, preorder=None):
        if preorder is None:
            preorder = range(6)
        if self.turn == 0:
            for i in preorder:
                if self.board[i] > 0:
                    yield i
        else:
            for i in preorder:
                if self.board[7+i] > 0:
                    yield i

    def print(self):
        print("   " + str(self.p2_pits[5]) + " " + str(self.p2_pits[4]) + " " + str(self.p2_pits[3]) +
         " " + str(self.p2_pits[2]) + " " + str(self.p2_pits[1]) + " " + str(self.p2_pits[0]))
        print("" + str(self.p2_pot) + "\t\t  " + str(self.p1_pot))
        print("   " + str(self.p1_pits[0]) + " " + str(self.p1_pits[1]) + " " + str(self.p1_pits[2]) +
         " " + str(self.p1_pits[3]) + " " + str(self.p1_pits[4]) + " " + str(self.p1_pits[5]))

    def printSpaced(self):
        #A spaced out printing method so that opt actually shows correctly
        print("   " + str(self.p2_pits[5]) + "   " + str(self.p2_pits[4]) + "   " + str(self.p2_pits[3]) +
         "   " + str(self.p2_pits[2]) + "   " + str(self.p2_pits[1]) + "   " + str(self.p2_pits[0]))
        print("" + str(self.p2_pot) + "\t\t\t  " + str(self.p1_pot))
        print("   " + str(self.p1_pits[0]) + "   " + str(self.p1_pits[1]) + "   " + str(self.p1_pits[2]) +
         "   " + str(self.p1_pits[3]) + "   " + str(self.p1_pits[4]) + "   " + str(self.p1_pits[5]))

    @property
    def trace(self):
        return ''.join(str(move) for move in self._trace)

    @property
    def state(self):
        return hash(tuple(self.board))
