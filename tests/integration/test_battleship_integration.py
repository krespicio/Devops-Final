import unittest
from flaskr.Battleship import Battleship

# class BattleshipInit(unittest.TestCase):
#     def test_has_ship(self):
#         test_ship = Ship([0,1],2)
#         self.assertEqual(len(test_ship.stable), 2)
#         assert "01" in test_ship.stable
#         assert "02" in test_ship.stable
    
#     def test_ship_valid(self):
#         test_ship = Ship([1,1],3, True)
#         self.assertEqual(len(test_ship.stable), 3)
#         assert "11" in test_ship.stable
#         assert "21" in test_ship.stable
#         assert "31" in test_ship.stable

class BattleshipValidation(unittest.TestCase):
    def test_valid(self):
        test_game = Battleship()
        output = test_game.validateInput(0,0)
        self.assertTrue(output)

    def test_invalid_row(self):
        test_game = Battleship()
        output = test_game.validateInput(8,2)
        self.assertFalse(output)
    
    def test_invalid_col(self):
        test_game = Battleship()
        output = test_game.validateInput(1,9)
        self.assertFalse(output)

    def test_invalid_both(self):
        test_game = Battleship()
        output = test_game.validateInput(10,7)
        self.assertFalse(output)

# class BattleshipCheckResult(unittest.TestCase):
#     def test_valid(self):
#         test_game = Battleship()
#         output = test_game.validateInput(0,0)
#         self.assertTrue(output)

#     def test_invalid_row(self):
#         test_game = Battleship()
#         output = test_game.validateInput(8,2)
#         self.assertFalse(output)
    
#     def test_invalid_col(self):
#         test_game = Battleship()
#         output = test_game.validateInput(1,9)
#         self.assertFalse(output)

#     def test_invalid_both(self):
#         test_game = Battleship()
#         output = test_game.validateInput(10,7)
#         self.assertFalse(output)