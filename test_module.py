import unittest
from RPS import player

class UnitTests(unittest.TestCase):
    def test_player(self):
        self.assertEqual(player(""), "R")  # Beispieltest, passt den Test entsprechend an
        self.assertIn(player("R"), ["R", "P", "S"])

if __name__ == "__main__":
    unittest.main()
