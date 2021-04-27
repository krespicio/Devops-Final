import unittest
from flaskr.Battleship import Battleship

class BattleshipRowVal(unittest.TestCase):
    def test_valid(self):
        test_game = Battleship()
        output = test_game.validateRow(0)
        self.assertTrue(output)

    def test_invalid(self):
        test_game = Battleship()
        output = test_game.validateRow(8)
        self.assertFalse(output)

class BattleshipColVal(unittest.TestCase):
    def test_valid(self):
        test_game = Battleship()
        output = test_game.validateCol(0)
        self.assertTrue(output)

    def test_invalid(self):
        test_game = Battleship()
        output = test_game.validateRow(6)
        self.assertFalse(output)

class BattleshipRowVal(unittest.TestCase):
    def test_valid(self):
        test_game = Battleship()
        output = test_game.validateRow(0)
        self.assertTrue(output)

    def test_invalid(self):
        test_game = Battleship()
        output = test_game.validateRow(8)
        self.assertFalse(output)

# class BattleshipDisplay(unittest.TestCase):
#     def test_valid(self):
#         test_game = Battleship()
#         output = test_game.validateCol(0)
#         self.assertTrue(output)

#     def test_invalid(self):
#         test_game = Battleship()
#         output = test_game.validateRow(6)
#         self.assertFalse(output)