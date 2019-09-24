# tests/test_game.py
import unittest
import string
from game import Game

class TestGame(unittest.TestCase):
    def test_game_initialization(self):
        new_game = Game()
        grid = new_game.grid
        self.assertIsInstance(grid, list)
        self.assertEqual(len(grid), 9)
        for letter in grid:
            self.assertIn(letter, string.ascii_uppercase)

    def test_game_isvalid(self):
        new_game = Game()
        new_game.grid = ["K","W","I","E","N","F", "U", "Q", "W"]
        grid = new_game.grid
        self.assertIs(True, new_game.is_valid("FEUN"))



    def test_game_isinvalid(self):
        new_game = Game()
        new_game.grid = ["K","W","I","E","N","F", "U", "Q", "W"]
        grid = new_game.grid
        self.assertIs(False, new_game.is_valid("FAUN"))

    def test_empty_word_is_invalid(self):
        new_game = Game()
        self.assertIs(new_game.is_valid(''), False)

    def test_unknown_word_is_invalid(self):
      new_game = Game()
      new_game.grid = list('KWIENFUQW') # Force the grid to a test case:
      self.assertIs(new_game.is_valid('FEUN'), False)

