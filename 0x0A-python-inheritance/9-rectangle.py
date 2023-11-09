#!/usr/bin/python3
"""Defines the Rectangle class."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A subclass representing a rectangle."""

    def __init__(self, width, height):
        """Intialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
         """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """String representation method."""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
