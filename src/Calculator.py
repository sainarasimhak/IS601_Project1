import math


def addition(a, b):
    a = int(a)
    b = int(b)
    c = a + b
    return c


def subtraction(a, b):
    a = int(a)
    b = int(b)
    c = a - b
    return c


def multiplication(a, b):
    a = int(a)
    b = int(b)
    c = a * b
    return c


def division(a, b):
    a = int(a)
    b = int(b)
    c = float(a / b)
    return c


def square(a):
    a = int(a)
    b = (a * a)
    return b


def squareroot(a):
    a = int(a)
    b = math.sqrt(a)
    return b


class Calculator:

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def division(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result

    def squareroot(self, a):
        self.result = squareroot(a)
        return self.result
