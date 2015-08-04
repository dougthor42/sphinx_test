# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 09:40:44 2015

@author: dthor
"""


class BaseClass(object):
    """
    Base class for exmaples
    """
    def __init__(self):
        """
        No Doc
        """
        pass

    def run(self):
        """
        Run Doc
        """
        pass


class Child(BaseClass):
    """
    Child Class
    """
    def __init__(self):
        """
        Child class ``__init__`` doc
        """
        pass


def my_func(a, b, c):
    """
    This is my function

    There are many like it, but this one is mine.

    Parameters:
    -----------
    a : int
        Stuff

    b : float
        Something

    c : string
        Things

    Returns:
    --------
    value : string
        returns value

    """
    return a


def other_func(a):
    """
    Function #2

    :param int a: Stuff
    :param b: Things
    :type b: int, float, or iterable
    :return: Some String
    :rtype: str
    :raises TypeError: You're dumb
    """
    pass


def main():
    """
    Main program
    """
    a = my_func(1, 2, 3)
    print(a)

if __name__ == "__main__":
    main()
