#!/usr/bin/python3
"""class definiton for square shape object"""


class square():
    """class square define geometery shape  square"""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """constructor the class Square instances"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """find the perimeter of a square"""
        return (self.width * 4)

    def __str__(self):
        """stdio representee"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """test run square model"""
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
