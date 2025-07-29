import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):      #raise ZeroDivisionError if a == 0
    if a == 0:
        raise ZeroDivisionError('Cannot divide by zero.')
    return b / a

def log(a, b):      #raise ValueError
    if a <= 0 or a == 1:
        raise ValueError('Base a must be positive and not equal to 1.')
    if b <= 0:
        raise ValueError('Value b must be positive.')
    return math.log(a, b)

def exp(a, b):
    return a ** b

