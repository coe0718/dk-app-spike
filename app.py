import numbers


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def median(values):
    """Return the median of an iterable of numbers (read once).

    Odd count: the middle value. Even count: the mean of the two middle
    values, as a float. Raises ValueError("median of nothing") when empty,
    and TypeError for a bool or any non-number.
    """
    items = list(values)
    for v in items:
        if isinstance(v, bool) or not isinstance(v, numbers.Real):
            raise TypeError(f"median needs numbers, got {type(v).__name__}")
    if not items:
        raise ValueError("median of nothing")
    items.sort()
    n = len(items)
    mid = n // 2
    if n % 2:
        return items[mid]
    return float((items[mid - 1] + items[mid]) / 2)
