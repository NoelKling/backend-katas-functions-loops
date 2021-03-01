#!/usr/bin/env python
"""Implements math functions without using operators,
except for '+' and '-'.
"""

__author__ = "Noel Kling"


def add(x, y):
    """Add two integers."""
    return x + y


def sub(x, y):
    """ Substracts two integers """
    return x - y


def multiply(x, y):
    """Multiply x with y using the add() function above."""
    result = 0
    if x >= 0 and y >= 0:
        for i in range(y):
            result = add(result, x)
    elif x < 0 and y < 0:
        for i in range(abs(y)):
            result = add(result, abs(x))
    else:
        for i in range(abs(y)):
            result = add(result, abs(x))
        result = -result
    return result


def power(x, n):
    """Raise x to power n, where n >= 0, using the functions above."""
    if not n == 0:
        result = x
        for i in range(1, n):
            result = multiply(result, x)
        return result
    return 1


def factorial(x):
    """Compute the factorial of x, where x > 0, using the functions above."""
    result = x
    if not x == 0:
        for i in range(sub(x, 1), 0, -1):
            result = multiply(result, i)
        return result
    return 1


def fibonacci(n):
    """Compute the nth term of fibonacci sequence using the functions above."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = [0, 1]
        for i in range(2, add(n, 1)):
            result.append(add(result[sub(i, 2)], result[sub(i, 1)]))
        return result[n]


if __name__ == '__main__':
    
    pass
