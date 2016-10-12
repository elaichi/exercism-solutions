"""
http://exercism.io/exercises/python/leap/readme
"""


def is_leap_year(year):
    """
    https://en.wikipedia.org/wiki/Leap_year#Algorithm
    """
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
