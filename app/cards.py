from abc import ABC


class Card(ABC):
    def __init__(self, name: str, value: int):
        self._name = name
        self._value = value

    def get_value(self):
        return self._value

    def __str__(self):
        return self._name


class Ace(Card):
    def __init__(self):
        super().__init__('A', 1)


class Two(Card):
    def __init__(self):
        super().__init__('2', 2)


class Three(Card):
    def __init__(self):
        super().__init__('3', 3)


class Four(Card):
    def __init__(self):
        super().__init__('4', 4)


class Five(Card):
    def __init__(self):
        super().__init__('5', 5)


class Six(Card):
    def __init__(self):
        super().__init__('6', 6)


class Seven(Card):
    def __init__(self):
        super().__init__('7', 7)


class Eight(Card):
    def __init__(self):
        super().__init__('8', 8)


class Nine(Card):
    def __init__(self):
        super().__init__('9', 9)


class Ten(Card):
    def __init__(self):
        super().__init__('10', 10)


class K(Card):
    def __init__(self):
        super().__init__('K', 10)


class J(Card):
    def __init__(self):
        super().__init__('J', 10)


class Q(Card):
    def __init__(self):
        super().__init__('Q', 10)
