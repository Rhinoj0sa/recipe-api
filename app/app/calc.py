"""
Calculator functions
"""


def add(x, y):
    """Add x and y and return result."""
    return x + y


def subtract(x, y):
    """Subtract y from x and return result."""
    return x - y

values = {'a': 1, 'b': 2, 'c': 3}
def side_effect(arg):
    return values[arg]

mock.side_effect = side_effect
mock('a'), mock('b'), mock('c')

mock.side_effect = [5, 4, 3, 2, 1]
mock(), mock(), mock()