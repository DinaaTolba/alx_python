'''size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0'''
class Square:
    """
    This class represents a square.

    Attributes:
        size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initializes a new Square instance with a given size.
    """

    # Class attribute, not really needed in this case
    size = 0

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is less than 0.
        """
        # Validate the size
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size


    def area(self):
        area= self.__size**2
        return area