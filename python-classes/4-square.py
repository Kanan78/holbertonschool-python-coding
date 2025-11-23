#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """This class defines a square by: (based on 3-square.py)"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size**2

    def my_print(self):
        for i in range(self.__size):
            print('#' * self.__size)
