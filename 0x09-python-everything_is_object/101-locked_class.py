#!/usr/bin/python3

"""Defines the locked class """


class LockedClass:
    """
    Prevent the user from instatiating new LockedClass attributes
    for anything but attributes called 'first_name'
    """

    __slots__ = ["first_name"]
