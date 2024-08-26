import math


class Calculator:
    def __init__(self):
        pass

    def factorial(self, n):
        """Calcula el factorial de un número."""
        return 1 if n == 0 else n * self.factorial(n - 1)

    def fibonacci(self, n):
        """Calcula el n-ésimo número de la secuencia de Fibonacci."""
        return n if n <= 1 else self.fibonacci(n - 1) + self.fibonacci(n - 2)

    def power(self, base, exponent):
        """Calcula la potencia de un número elevado a otro."""
        return base**exponent

    def exponential(self, value):
        """Calcula la función exponencial e^x."""
        return math.exp(value)

    def hyperbolic_sine(self, value):
        """Calcula el seno hiperbólico de un valor."""
        return math.sinh(value)
