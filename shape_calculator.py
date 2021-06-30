class Rectangle:
    def __init__(self, height, width) -> None:
        self.set_height(width)
        self.set_width(height)


    def set_width(self, width: int) -> None:
        self.width = width


    def set_height(self, height: int) -> None:
        self.height = height


    def get_area(self) -> int:
        return self.width * self.height


    def get_perimeter(self) -> int:
        return 2 * self.width + 2 * self.height


    def get_diagonal(self) -> int:
        return (self.width ** 2 + self.height ** 2) ** .5


    def get_picture(self) -> str:
        picture = '*'*self.width + '\n'
        for _ in range(self.height-1):
            picture += '*'*self.width + '\n'

        return picture

    def __str__(self) -> str:
        return '{}(width={}, height={})'.format(self.__class__.__name__,
                                                str(self.width),
                                                str(self.height))


class Square(Rectangle):
    def __init__(self, side) -> None:
        self.width = side
        self.height = side


    def set_side(self, side):
        self.set_height(side)
        self.set_width(side)

    
    def __str__(self) -> str:
        return '{}(side={})'.format(self.__class__.__name__,
                                    str(self.width))


rect = Rectangle(5, 10)
print(rect.get_picture())
