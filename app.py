import numbers


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def mean(values):
    """Arithmetic mean of an iterable of real numbers, as a float.

    The iterable is consumed exactly once. bool is rejected (it is an int
    subclass but not a number here), as is any non-real value.
    """
    total = 0
    count = 0
    for v in values:
        if isinstance(v, bool) or not isinstance(v, numbers.Real):
            raise TypeError(f"mean needs numbers, got {type(v).__name__}")
        total += v
        count += 1
    if count == 0:
        raise ValueError("mean of no values")
    return float(total / count)


def divide(a, b):
    if b == 0:
        raise ValueError("cannot divide by zero: b must be non-zero")
    return a / b
