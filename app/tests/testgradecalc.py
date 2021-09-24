# Use unittest library to create a unit test method to test the calculate_avg_grade function created in the gradecalc module
# Make sure you include multiple unit tests to test that the function acts as expected in different scenarios
import unittest


from app.src.Student import Student
from app.src.gradecalc import calculate_avg_grade

class test_gradecalc(unittest):

    def test_grade(self):
        input=[Student('s1',20,1824,90.5), Student('s2',21,1823,80.0), Student('s1',20,1824,70.0)]
        actual=calculate_avg_grade(input)
        self.assertEqual(expected, actual)
        self.assertTrue(isinstance(actual, float))