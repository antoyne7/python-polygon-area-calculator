class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def set_width(self, width: int) -> None:
        self.width = width

    def set_height(self, height: int) -> None:
        self.height = height

    def get_area(self) -> int:
        return self.width * self.height

    def get_perimeter(self) -> int:
        return 2 * self.width + 2 * self.height

    def get_diagonal(self) -> float:
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self) -> str:
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'

        picture = '*'*self.width + '\n'
        for _ in range(self.height-1):
            picture += '*'*self.width + '\n'

        return picture
    
    def get_amount_inside(self, rectangle) -> int:
        amount_width = self.width // rectangle.width
        amount_height = self.height // rectangle.height
        return amount_width * amount_height

    def __str__(self) -> str:
        return '{}(width={}, height={})'.format(self.__class__.__name__,
                                                str(self.width),
                                                str(self.height))


class Square(Rectangle):
    def __init__(self, side) -> None:
        super().__init__(side, side)

    def set_side(self, side) -> None:
        self.width = side
        self.height = side

    def set_width(self, width) -> None:
        self.set_side(width)

    def set_height(self, height) -> None:
        self.set_side(height)
    
    def __str__(self) -> str:
        return '{}(side={})'.format(self.__class__.__name__,
                                    str(self.width))
