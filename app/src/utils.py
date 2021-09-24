# Create a function called calculate_avg
# Parameters: the function should have one argument of type list of floats (i.e., the arg should be a list of numbers with decimals)
# Returns: the function should return a float: the average of all the numbers that are given in the list as an argument to this function.
#          The returned value should be rounded to the closest second decimal. Use the build-in round function: https://www.w3schools.com/python/ref_func_round.asp
#
# If the argument is an empty list, raise a new expcetion with the message: 'expected a non-empty list'
# for reference on exceptions, check the class notes here: https://github.com/FTEC-6v99/python-overview/blob/master/advanced/exceptions.py
#
# Make sure that you add type hints to the function paramter and return value
import typing as t


def calculate_avg(grades: list[t.Union[int, float]]) -> float:
    total: float = 0.0
    for grade in grades:
        total += grade

    return round(total / len(grades), 2)