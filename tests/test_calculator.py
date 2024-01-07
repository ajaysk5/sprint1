import unittest

import pytest

from hypothesis import given, assume
import hypothesis.strategies as st
import math
from calculator.module import CalculatorClass


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = CalculatorClass(25)

    def test_add(self):
        self.assertEqual(self.calc.add(2), 27)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2), 23)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2.0), 50)

    def test_divide(self):
        self.assertEqual(self.calc.divide(5), 5)

    def test_root(self):
        self.assertEqual(self.calc.root(2), 5)

    def test_reset(self):
        self.assertEqual(self.calc.reset_memory(), 25)


calc_instance = CalculatorClass(25)


# pytest test cases


def test_add():
    assert calc_instance.add(25) == 50, "Should be 50"


def test_subtract():
    assert calc_instance.subtract(25) == 25, "Should be 0"


def test_multiply():
    assert calc_instance.multiply(2.0) == 50, "Should be 50"


def test_divide():
    assert calc_instance.divide(5.0) == 10, "Should be 5"


def test_root():
    assert calc_instance.root(2) == 3.1622776601683795, "Should be 5"


def test_reset():
    assert calc_instance.reset_memory() == 25, "Should be 25"


def test_add_types():
    with pytest.raises(TypeError):
        calc_instance.add('hello')


def test_subtract_types():
    with pytest.raises(TypeError):
        calc_instance.subtract('hello')


def test_multiply_types():
    with pytest.raises(TypeError):
        calc_instance.multiply('hello')


def test_divide_types():
    with pytest.raises(TypeError):
        calc_instance.divide('world')


def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        calc_instance.divide(0)

# Hypothesis testing


class TestCalculatorClass(unittest.TestCase):

    @given(st.floats(), st.floats())
    def test_add(self, initial_memory, num):
        calcu_instance = CalculatorClass(initial_memory)
        result = calcu_instance.add(num)
        if math.isnan(result) or math.isinf(result):
            self.assertTrue(math.isnan(initial_memory + num) or math.isinf(initial_memory + num))
        else:
            self.assertEqual(result, initial_memory + num)

    @given(st.floats(), st.floats())
    def test_subtract(self, initial_memory, num):
        calcu_instance = CalculatorClass(initial_memory)
        result = calcu_instance.subtract(num)
        if math.isnan(result) or math.isinf(result):
            self.assertTrue(math.isnan(initial_memory - num) or math.isinf(initial_memory - num))
        else:
            self.assertEqual(result, initial_memory - num)

    @given(st.floats(), st.floats(allow_nan=False, allow_infinity=False))
    def test_multiply(self, initial_memory, num):
        calcu_instance = CalculatorClass(initial_memory)
        result = calcu_instance.multiply(num)
        if math.isnan(result) or math.isinf(result):
            self.assertTrue(math.isnan(initial_memory * num) or math.isinf(initial_memory * num))
        else:
            self.assertEqual(result, initial_memory * num)

    @given(st.floats(), st.floats(allow_nan=False, allow_infinity=False))
    def test_divide(self, initial_memory, num):
        # Avoid division by zero in hypothesis
        assume(num != 0)
        calcu_instance = CalculatorClass(initial_memory)
        result = calcu_instance.divide(num)
        if math.isnan(result) or math.isinf(result):
            self.assertTrue(math.isnan(initial_memory / num) or math.isinf(initial_memory / num))
        else:
            self.assertEqual(result, initial_memory / num)

    @given(st.floats(allow_nan=False, allow_infinity=False), st.integers(min_value=1))
    def test_root(self, initial_memory, n):
        assume(initial_memory == float())
        calcu_instance = CalculatorClass(initial_memory)
        result = calcu_instance.root(n)
        if math.isnan(result) or math.isinf(result):
            self.assertTrue(math.isnan(initial_memory ** (1 / n)) or math.isinf(initial_memory ** (1 / n)))
        else:
            self.assertEqual(result, initial_memory ** (1 / n))

    @given(st.floats())
    def test_reset_memory(self, initial_memory):
        assume(initial_memory != math.nan and initial_memory == float() and initial_memory != math.inf)
        calcu_instance = CalculatorClass(initial_memory)
        result = calcu_instance.reset_memory()
        self.assertEqual(result, calcu_instance.initial_memory)


if __name__ == "__main__":
    unittest.main()
