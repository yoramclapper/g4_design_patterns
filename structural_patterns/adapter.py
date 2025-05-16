from abc import ABC, abstractmethod

class Manipulator:
    pass

class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def bounding_box(self, bottom_left: tuple, top_right: tuple) -> tuple:
        """Calculate the bounding box of the shape."""
        pass

    @abstractmethod
    def create_manipulator(self) -> Manipulator:
        """Create a manipulator for the shape."""
        pass


class TextView:

    def __init__(self, x: int, y: int, width: int, height: int):
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def get_origin(self) -> tuple:
        return self._x, self._y

    def get_extent(self) -> tuple:
        return self._width, self._height

    def is_empty(self) -> bool:
        return self._width == 0 or self._height == 0


class TextShape(Shape, TextView):

    def __init__(self, x: int, y: int, width: int, height: int):
        TextView.__init__(self, x, y, width, height)

    def bounding_box(self, bottom_left: tuple, top_right: tuple) -> tuple:
        """Calculate the bounding box of the text shape."""
        x, y = self.get_origin()
        width, height = self.get_extent()
        bottom_left = (x, y)
        top_right = (x + width, y + height)
        return bottom_left, top_right

    def create_manipulator(self) -> Manipulator:
        """Create a manipulator for the text shape."""
        return Manipulator()


if __name__ == "__main__":
    text_shape = TextShape(10, 20, 100, 50)
    print("Bounding Box:", text_shape.bounding_box((0, 0), (0, 0)))
    print("Manipulator:", text_shape.create_manipulator())
    print("Is Empty:", text_shape.is_empty())