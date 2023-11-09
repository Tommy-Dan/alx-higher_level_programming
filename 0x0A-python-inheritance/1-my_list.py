#!/usr/bin/python3
"""Defines an inherited list class for MyList."""


class MyList(list):
    """Custom MyList class."""
    def print_sorted(self):
        """Method for printing sorted list."""
        print(sorted(self))
