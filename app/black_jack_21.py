import os
import time
from functools import reduce

from app.cards import Ace, Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten, K, Q, J
from app.deck import Deck
from app.player import Player


class BlackJack21(object):
    def __init__(self, player: Player):
        _cards = [
            Ace(),
            Two(),
            Three(),
            Four(),
            Five(),
            Six(),
            Seven(),
            Eight(),
            Nine(),
            Ten(),
            K(),
            Q(),
            J(),
        ]
        self._deck = Deck(_cards)
        self._player = player
        self._tapped_cards = []
        self._score = 0

    def start(self):
        _loading()
        print('==== Embaralhando ====')
        self._deck.shuffle()
        time.sleep(1.5)
        _clear()
        print('==== Mesa pronta, podemos começar ====')
        while self._deck.has_more_cards():
            input('---- Pressione ENTER para virar uma carta jogador {} ----'.format(self._player))
            tapped_card = self._deck.put_card()
            self._tapped_cards.append(tapped_card)
            print('---- Carta virada ----', tapped_card)
            print(' Calculando ...')
            self._calculate_score()
            if self._is_done():
                break
            print('=== Pontuação {} ===='.format(self._score))
        self._finish()

    def _is_done(self):
        if self._score <= 21:
            return False
        return True

    def _calculate_score(self):
        self._score = sum(map(lambda card: card.get_value(), self._tapped_cards))

    def _finish(self):
        _clear()
        print('==== Acabou o jogo ====')
        print('==== Calculando ====')
        _loading()
        _clear()
        print('O Resultado é: {}'.format(self._score))


def _loading():
    for i in range(10, 101, 10):
        print('Carregando {} %'.format(i))
        time.sleep(0.2)


def _clear():
    os.system('cls' if os.name == 'nt' else 'clear')
