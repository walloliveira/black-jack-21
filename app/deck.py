import random


class Deck:
    def __init__(self, cards: list):
        self._cards = cards

    def get_cards(self):
        return self._cards.copy()

    def shuffle(self):
        random.shuffle(self._cards)

    def put_card(self):
        if not self.has_more_cards():
            raise Exception('No more cards. =(')
        return self._cards.pop(0)

    def has_more_cards(self):
        return len(self._cards)
