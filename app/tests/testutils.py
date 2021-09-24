# Create a unit test method to test the calculate_avg function created in the utils module
# Make sure you include multiple unit tests to test that the function acts as expected in different scenarios
import unittest

from app.src.utils import calculate_avg


class utils_validator(unittest.TestCase):

    def test_calc_avg(self):
        input= [1,1,1,1]
        expected=1
        actual=calculate_avg(input)
        self.assertEqual(expected, actual)
        self.assertTrue(isinstance(actual, float))

    def test_calc_avg_bad_input_type(self):
        input = ['s', 'f']
        self.assertRaises(TypeError, calculate_avg, input)

    def test_calc_avg_empty_list(self):
        self.assertRaises(Exception, calculate_avg, [])