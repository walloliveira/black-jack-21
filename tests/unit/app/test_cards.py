import unittest

from app.cards import Ace, Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten, Q, J, K


class TestCards(unittest.TestCase):
    def test_ace_should_be_value_1_and_name_is_A(self):
        card = Ace()
        self.assertEqual(card.get_value(), 1, 'Valor do ACE deveria ser 1')
        self.assertEqual(card.__str__(), 'A', 'Nome da carta Ace deveria ser A')

    def test_two_should_be_value_2_and_name_is_2(self):
        card = Two()
        self.assertEqual(card.get_value(), 2)
        self.assertEqual(card.__str__(), '2')

    def test_three_should_be_value_3_and_name_is_3(self):
        card = Three()
        self.assertEqual(card.get_value(), 3)
        self.assertEqual(card.__str__(), '3')

    def test_four_should_be_value_4_and_name_is_4(self):
        card = Four()
        self.assertEqual(card.get_value(), 4)
        self.assertEqual(card.__str__(), '4')

    def test_five_should_be_value_5_and_name_is_5(self):
        card = Five()
        self.assertEqual(card.get_value(), 5)
        self.assertEqual(card.__str__(), '5')

    def test_six_should_be_value_6_and_name_is_6(self):
        card = Six()
        self.assertEqual(card.get_value(), 6)
        self.assertEqual(card.__str__(), '6')

    def test_seven_should_be_value_7_and_name_is_7(self):
        card = Seven()
        self.assertEqual(card.get_value(), 7)
        self.assertEqual(card.__str__(), '7')

    def test_eight_should_be_value_8_and_name_is_8(self):
        card = Eight()
        self.assertEqual(card.get_value(), 8)
        self.assertEqual(card.__str__(), '8')

    def test_nine_should_be_value_9_and_name_is_9(self):
        card = Nine()
        self.assertEqual(card.get_value(), 9)
        self.assertEqual(card.__str__(), '9')

    def test_ten_should_be_value_10_and_name_is_10(self):
        card = Ten()
        self.assertEqual(card.get_value(), 10)
        self.assertEqual(card.__str__(), '10')

    def test_Q_should_be_value_10_and_name_is_Q(self):
        card = Q()
        self.assertEqual(card.get_value(), 10)
        self.assertEqual(card.__str__(), 'Q')

    def test_J_should_be_value_10_and_name_is_J(self):
        card = J()
        self.assertEqual(card.get_value(), 10)
        self.assertEqual(card.__str__(), 'J')

    def test_K_should_be_value_10_and_name_is_K(self):
        card = K()
        self.assertEqual(card.get_value(), 10)
        self.assertEqual(card.__str__(), 'K')
