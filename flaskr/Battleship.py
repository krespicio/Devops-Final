import random
from .Ship import Ship

class Battleship:
    def __init__(self, isRandom=True, pos=[]):
        self.grid = [["0" for i in range(5)] for j in range(4)]
        row = random.randint(0,1)
        col = random.randint(0,3)
        if not isRandom and len(pos) == 2:
            row = pos[0]
            col = pos[1]
        self.ship = Ship([row,col],3)
        self.win = False

    def displayGrid(self):
        for row in self.grid:
            print("\t".join(row))
        print()

    def validateRow(self,row):
        if type(row) != int and not row.isdigit():
            return False
        elif int(row) < 0 or int(row) > 3:
            return False
        return True

    def validateCol(self,col):
        if type(col) != int and not col.isdigit():
            return False
        elif int(col) < 0 or int(col) > 4:
            return False
        return True

    def validateInput(self, row, col):
        return self.validateCol(col) and self.validateRow(row)

    def checkResult(self, row, col):
        if self.ship.hit([row, col]):
            self.grid[row][col] = "S"
            self.win = len(self.ship.stable) == 0
        else:
            self.grid[row][col] = "X"

        return self.win