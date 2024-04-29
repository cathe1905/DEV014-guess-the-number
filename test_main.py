"""
This is the test !!!
"""
import unittest
from app import get_guess_computer, get_guess_player, mainFunction
from unittest.mock import patch, MagicMock, Mock

class TestMainCode(unittest.TestCase):
    
    def test_get_computer(self):
            result = get_guess_computer()
            self.assertGreaterEqual(result, 1)
            self.assertLessEqual(result, 100)    

    @patch('builtins.input', return_value="22")
    def test_get_player_returns_int(self, mock_input):
            result= get_guess_player()
            self.assertEqual(result, 22)

    # def test_main_function(self):
    #     mainFunction()
    #     get_guess_player.assert_called_once()

    @patch('app.mainFunction', return_value=False)
    def test_main_function2(self, mock_main):
        result = mock_main()  
        self.assertFalse(result, "the function doesn't work properly")
        get_guess_player.assert_called_once()
          

if __name__ == '__main__':
    unittest.main()
    