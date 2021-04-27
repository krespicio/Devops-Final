import unittest
from flaskr.Ship import Ship

class ShipInit(unittest.TestCase):
    def test_col(self):
        test_ship = Ship([0,1],2)
        self.assertEqual(len(test_ship.stable), 2)
        assert "01" in test_ship.stable
        assert "02" in test_ship.stable
    
    def test_row(self):
        test_ship = Ship([1,1],3, True)
        self.assertEqual(len(test_ship.stable), 3)
        assert "11" in test_ship.stable
        assert "21" in test_ship.stable
        assert "31" in test_ship.stable

class ShipHit(unittest.TestCase):
    def test_hit(self):
        test_ship = Ship([1,1],3, True)
        output = test_ship.hit([1,1])
        self.assertEqual(len(test_ship.stable), 2)
        self.assertEqual(len(test_ship.destroyed), 1)
        assert "11" not in test_ship.stable
        assert "11" in test_ship.destroyed
        self.assertTrue(output)

    def test_no_hit(self):
        test_ship = Ship([1,1],3, True)
        output = test_ship.hit([0,0])
        self.assertEqual(len(test_ship.stable), 3)
        self.assertEqual(len(test_ship.destroyed), 0)
        self.assertFalse(output)
