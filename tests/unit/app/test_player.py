import unittest

from app.player import Player


class TestPlayer(unittest.TestCase):
    def test_player_should_be_name_equal_Test(self):
        card = Player('Test')
        self.assertEqual(card.__str__(), 'Test')
