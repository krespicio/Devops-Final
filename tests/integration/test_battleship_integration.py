import unittest
from flaskr.Battleship import Battleship

# Relies on the ship class
class BattleshipInit(unittest.TestCase):
    def test_has_ship(self):
        test_game = Battleship(isRandom=False, pos=[1,1])
        self.assertGreater(len(test_game.ship.stable), 0)
    
    def test_ship_valid(self):
        test_game = Battleship(isRandom=False, pos=[1,1])
        self.assertEqual(len(test_game.ship.stable), 3)
        assert "11" in test_game.ship.stable
        assert "12" in test_game.ship.stable
        assert "13" in test_game.ship.stable

# Validation relies on two other functions
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

class BattleshipCheckResult(unittest.TestCase):
    def test_proper_gameplay(self):

        # Init the ship
        test_game = Battleship(isRandom=False, pos=[1,1])

        # Input some bad hits
        shipDestroyed = test_game.checkResult(0,0)
        self.assertFalse(shipDestroyed)
        self.assertEqual(test_game.grid[0][0], "X")

        shipDestroyed = test_game.checkResult(3,2)
        self.assertFalse(shipDestroyed)
        self.assertEqual(test_game.grid[3][2], "X")

        shipDestroyed = test_game.checkResult(0,1)
        self.assertFalse(shipDestroyed)
        self.assertEqual(test_game.grid[0][1], "X")

        shipDestroyed = test_game.checkResult(2,2)
        self.assertFalse(shipDestroyed)
        self.assertEqual(test_game.grid[2][2], "X")

        # Input some good hits
        shipDestroyed = test_game.checkResult(1,1)
        self.assertFalse(shipDestroyed)
        self.assertEqual(test_game.grid[1][1], "S")

        shipDestroyed = test_game.checkResult(1,2)
        self.assertFalse(shipDestroyed)
        self.assertEqual(test_game.grid[1][2], "S")

        # Final hit should activates win condition
        shipDestroyed = test_game.checkResult(1,3)
        self.assertEqual(test_game.grid[1][3], "S")
        self.assertTrue(shipDestroyed)