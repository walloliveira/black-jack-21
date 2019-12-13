import unittest
from unittest.mock import Mock, patch, MagicMock

from app.black_jack_21 import BlackJack21


class TestBlackJack21(unittest.TestCase):

    @patch('app.black_jack_21.input')
    @patch('app.black_jack_21.time')
    @patch('app.black_jack_21.print')
    def test_black_jack_21_should_be_start_game(self, print_mock, time_mock, input_mock):
        player_mock = Mock()
        time_mock.sleep = MagicMock()

        black_jack_21 = BlackJack21(player_mock)

        black_jack_21.start()

        self.assertTrue(print_mock.called)
        self.assertTrue(input_mock.called)
        self.assertEqual(time_mock.sleep.call_count, 21)

        mock_calls = time_mock.sleep.mock_calls

        sleep_1 = mock_calls[0].args[0]
        sleep_2 = mock_calls[1].args[0]
        sleep_3 = mock_calls[2].args[0]
        sleep_4 = mock_calls[3].args[0]
        sleep_5 = mock_calls[4].args[0]
        sleep_6 = mock_calls[5].args[0]
        sleep_7 = mock_calls[6].args[0]
        sleep_8 = mock_calls[7].args[0]
        sleep_9 = mock_calls[8].args[0]
        sleep_10 = mock_calls[9].args[0]
        sleep_11 = mock_calls[10].args[0]

        self.assertEqual(sleep_1, 0.2)
        self.assertEqual(sleep_2, 0.2)
        self.assertEqual(sleep_3, 0.2)
        self.assertEqual(sleep_4, 0.2)
        self.assertEqual(sleep_5, 0.2)
        self.assertEqual(sleep_6, 0.2)
        self.assertEqual(sleep_7, 0.2)
        self.assertEqual(sleep_8, 0.2)
        self.assertEqual(sleep_9, 0.2)
        self.assertEqual(sleep_10, 0.2)
        self.assertEqual(sleep_11, 1.5)
