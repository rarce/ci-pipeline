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


if __name__ == "__main__":
    calc = Calculator()
    print(calc.factorial(5))
    print(calc.fibonacci(5))
    print(calc.power(2, 3))
    print(calc.exponential(2))
    print(calc.hyperbolic_sine(2))
