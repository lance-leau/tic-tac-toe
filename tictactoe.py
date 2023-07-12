class State:
    def blank():
        return "  "

    def cross():
        return "✖ "

    def circle():
        return "〇"

class tictactoe:
    def __init__(self):
        self.grid = tictactoe.newGrid()

    def newGrid():
        grid = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append(State.blank())
            grid.append(row)
        return grid

    def setBox(self, x, y, state):
        self.grid[y][x] = state

    def prettyPrint(self):
        print("      ┃      ┃     ")
        print("  "+self.grid[0][0]+"  ┃  "+self.grid[1][0]+"  ┃  "+self.grid[2][0]+"  ")
        print("1     ┃2     ┃3    ")
        print("━━━━━━╋━━━━━━╋━━━━━━")
        print("      ┃      ┃     ")
        print("  "+self.grid[0][1]+"  ┃  "+self.grid[1][1]+"  ┃  "+self.grid[2][1]+"  ")
        print("4     ┃5     ┃6    ")
        print("━━━━━━╋━━━━━━╋━━━━━━")
        print("      ┃      ┃     ")
        print("  "+self.grid[0][2]+"  ┃  "+self.grid[1][2]+"  ┃  "+self.grid[2][2]+"  ")
        print("7     ┃8     ┃9    \n")

    def checkGameState(self):
        if self.grid[0][0] == self.grid[0][1] == self.grid[0][2] and self.grid[0][0] != State.blank():
            return self.grid[0][0]
        if self.grid[1][0] == self.grid[1][1] == self.grid[1][2] and self.grid[1][0] != State.blank():
            return self.grid[1][0]
        if self.grid[2][0] == self.grid[2][1] == self.grid[2][2] and self.grid[2][0] != State.blank():
            return self.grid[2][0]
        if self.grid[0][0] == self.grid[1][0] == self.grid[2][0] and self.grid[0][0] != State.blank():
            return self.grid[0][0]
        if self.grid[0][1] == self.grid[1][1] == self.grid[2][1] and self.grid[0][1] != State.blank():
            return self.grid[0][1]
        if self.grid[0][2] == self.grid[1][2] == self.grid[2][2] and self.grid[0][2] != State.blank():
            return self.grid[0][2]
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] and self.grid[0][0] != State.blank():
            return self.grid[0][0]
        if self.grid[2][0] == self.grid[1][1] == self.grid[0][2]:
            return self.grid[2][0]
        if self.checkGameDraw():
            return "draw"
        else:
            return State.blank()
    
    def checkGameDraw(self):
        for i in range(3):
            for j in range (3):
                if self.grid[i][j] == State.blank():
                    return False
        return True

    def getEmptyBox(self):
        ret = []
        for i in range(3):
            for j in range (3):
                if self.grid[i][j] == State.blank():
                    ret.append((j, i))
        return ret

    def checkMove(self, x, y):
        if x<0 or y<0 or x>2 or y>2 or self.grid[y][x] != State.blank():
            return False
        return True

    def setBoard(self, board):
        for i in range(3):
            for j in range (3):
                self.grid[i][j] = board[i][j]

    def deepCopy(self):
        copy = tictactoe()
        copy.setBoard(self.grid)
        return copy