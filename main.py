from app.black_jack_21 import BlackJack21
from app.player import Player

if __name__ == '__main__':
    print('==== Black Jack 21 ====')
    player = Player(input('Digite seu nome Jogador: '))
    black_jack_21 = BlackJack21(player)
    black_jack_21.start()
