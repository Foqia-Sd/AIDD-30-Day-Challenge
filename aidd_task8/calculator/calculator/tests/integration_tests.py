import unittest
from unittest.mock import patch
from io import StringIO
import sys

from calculator.main import main

class TestCalculatorIntegration(unittest.TestCase):

    @patch('builtins.input', side_effect=['5', '+', '3', 'q'])
    def test_addition(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            main()
            output = fake_stdout.getvalue()
            self.assertIn("Result: 8.0", output)

    @patch('builtins.input', side_effect=['10', '-', '4', 'q'])
    def test_subtract(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            main()
            output = fake_stdout.getvalue()
            self.assertIn("Result: 6.0", output)

    @patch('builtins.input', side_effect=['6', '*', '7', 'q'])
    def test_multiply(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            main()
            output = fake_stdout.getvalue()
            self.assertIn("Result: 42.0", output)

    @patch('builtins.input', side_effect=['10', '/', '2', 'q'])
    def test_division(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            main()
            output = fake_stdout.getvalue()
            self.assertIn("Result: 5.0", output)

    @patch('builtins.input', side_effect=['10', '/', '0', 'q'])
    def test_division_by_zero(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            main()
            output = fake_stdout.getvalue()
            self.assertIn("Error: Division by zero is not allowed.", output)

    @patch('builtins.input', side_effect=['abc', '5', '+', '3', 'q'])
    def test_invalid_numerical_input_first_number(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            main()
            output = fake_stdout.getvalue()
            self.assertIn("Error: Invalid input. Please enter a number.", output)
            self.assertIn("Result: 8.0", output)

    @patch('builtins.input', side_effect=['5', '+', 'xyz', '3', 'q'])
    def test_invalid_numerical_input_second_number(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            main()
            output = fake_stdout.getvalue()
            self.assertIn("Error: Invalid input. Please enter a number.", output)
            self.assertIn("Result: 8.0", output)

if __name__ == '__main__':
    unittest.main()
