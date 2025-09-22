from typing import Union

Number = Union[int, float]

class Calculator:
    """Core calculator logic"""

    @staticmethod
    def add(a: Number, b: Number) -> Number: return a + b
    @staticmethod
    def subtract(a: Number, b: Number) -> Number: return a - b
    @staticmethod
    def multiply(a: Number, b: Number) -> Number: return a * b
    @staticmethod
    def divide(a: Number, b: Number) -> Number:
        if b == 0: raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    @staticmethod
    def power(a: Number, b: Number) -> Number: return a ** b
    @staticmethod
    def percent(a: Number, b: Number) -> Number: return (a / 100.0) * b
    @staticmethod
    def negate(a: Number) -> Number: return -a
