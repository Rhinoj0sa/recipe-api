"""
Calculator functions
"""


def add(x, y):
    """Add x and y and return result."""
    return x + y


def subtract(x, y):
    """Subtract y from x and return result."""
    return x - y


values = {"a": 1, "b": 2, "c": 3}


def side_effect(arg):
    return values[arg]
