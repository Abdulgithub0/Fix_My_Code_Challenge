#!/usr/bin/python3
"""
class definiton for square shape object
"""


class Square():
    """class square define geometry  square"""
    _width = 0
    _height = 0

    def __init__(self, *args, **kwargs):
        """constructor the class Square instances"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def perimeter_of_square(self):
        """find the perimeter of a square"""
        return ((self.width * 2) + (self.height * 2))

    def __str__(self):
        """stdout representee"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """test run square model"""
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_square())
