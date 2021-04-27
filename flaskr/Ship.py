import random

# Represents a ship, used for battleship game
class Ship:
    def __init__(self, start, length, isCol=False):
        self.stable = set()
        self.destroyed = set()
        for x in range(length):
            if isCol:
                self.stable.add(str(start[0]+x) + str(start[1]))
            else:
                self.stable.add(str(start[0]) + str(start[1]+x))

    def hit(self, pos):
        stringPos = str(pos[0]) + str(pos[1])
        if(stringPos in self.stable):
            self.stable.remove(stringPos)
            self.destroyed.add(stringPos)
            return True
        return False
