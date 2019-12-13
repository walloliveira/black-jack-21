import unittest, pytest
from unittest.mock import Mock, patch, MagicMock

from app.deck import Deck


class TestDeck(unittest.TestCase):
    def test_deck_should_be_3_cards(self):
        cards = [
            Mock(),
            Mock(),
            Mock(),
        ]
        deck = Deck(cards)
        self.assertEqual(len(deck.get_cards()), 3)

    @patch('app.deck.random')
    def test_deck_should_be_shuffle_cards(self, random_mock):
        cards = [
            Mock(),
            Mock(),
            Mock(),
        ]
        random_mock.shuffle = MagicMock()
        deck = Deck(cards)

        deck.shuffle()

        random_mock.shuffle.assert_called_once_with(cards)

    def test_deck_should_be_put_a_card(self):
        cards = [
            Mock(),
            Mock(),
            Mock(),
        ]
        deck = Deck(cards)

        deck.put_card()

        self.assertEqual(len(deck.get_cards()), 2)

    def test_deck_should_be_throw_exception_no_more_cards(self):
        deck = Deck([])

        with pytest.raises(Exception) as ex:
            deck.put_card()

        self.assertEqual(str(ex.value), 'No more cards. =(')
