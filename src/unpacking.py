""" Fun with unpacking stuff. """

from typing import Any, Tuple


def print_integers(val01: int, val02: int) -> None:
    """ Prints some message for the integers. """
    print(f"--> print_integers() -- VAL 1 = {val01}, VAL 2 = {val02}")


def print_tuples(tup: tuple[Any, ...]) -> None:
    """ Prints some message for the tuple. """
    print(f"--> print_tuples() -- TUPLE = {tup}")


def get_tuples(val01: int, val02: int) -> Tuple[int, int]:
    """ Constructs a tuple out of integers. """
    return (val01, val02)


tup01: Tuple[int, int] = get_tuples(11, 14)
# --> print_tuples() -- TUPLE = (11, 14)
print_tuples(tup01)
# --> print_integers() -- VAL 1 = 11, VAL 2 = 14
print_integers(*tup01)

tup02 = (13, get_tuples(17, 19), 23)
# --> print_tuples() -- TUPLE = (13, (17, 19), 23)
print_tuples(tup02)

tup03 = (13, *get_tuples(17, 19), 23)
# --> print_tuples() -- TUPLE = (13, 17, 19, 23)
print_tuples(tup03)
