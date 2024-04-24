"""
This is the test !!!
"""
import unittest
from app import get_guess_computer, get_guess_Player, mainFunction
from unittest.mock import patch
import io
import random

class TestMainCode(unittest.TestCase):
    def test_get_computer(self):
        with patch('sys.stdout', new= io.StringIO()) as fake_out:
            result = get_guess_computer()
            self.assertIsInstance(result, int)
            self.assertGreaterEqual(result, 1)
            self.assertLessEqual(result, 100)
            self.assertEqual(fake_out.getvalue(), '')

    def test_get_player(self):
        with patch('sys.stdout', new= io.StringIO()) as fake_out:
            result= get_guess_Player()
            self.assertIsInstance(result, int)
            self.assertGreaterEqual(result, 1)
            self.assertLessEqual(result, 100)
            self.assertEqual(fake_out.getvalue(), '')

    def test_main_function(self):
      secret_number = random.randint(1, 100)
      with patch('sys.stdout', new=io.StringIO()) as fake_out:
        mainFunction(secret_number)
        print("Captured Output:", fake_out.getvalue())
        self.assertEqual(fake_out.getvalue(), '')

if __name__ == '__main__':
    unittest.main()
    