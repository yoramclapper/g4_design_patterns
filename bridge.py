# implemented own interpretation of the Bridge pattern because the book example is too convuluted

from abc import ABC, abstractmethod

class ColorPainter(ABC):

    @property
    @abstractmethod
    def color(self):
        pass

    @abstractmethod
    def paint(self):
        pass


class RedPainter(ColorPainter):
    def __init__(self):
        self._color = "red"

    @property
    def color(self):
        return self._color

    def paint(self):
        print(f"Painting in {self.color} color")


class BluePainter(ColorPainter):
    def __init__(self):
        self._color = "blue"

    @property
    def color(self):
        return self._color

    def paint(self):
        print(f"Painting in {self.color} color")


class Surface(ABC):

    def __init__(self, painter: ColorPainter):
        self._painter = painter

    @abstractmethod
    def draw(self):
        pass


class Door(Surface):

    def __init__(self, painter: ColorPainter):
        super().__init__(painter)

    def draw(self):
        print("Drawing a door")
        self._painter.paint()


class Wall(Surface):

    def __init__(self, painter: ColorPainter):
        super().__init__(painter)

    def draw(self):
        print("Drawing a wall")
        self._painter.paint()


if __name__ == "__main__":
    red_painter = RedPainter()
    blue_painter = BluePainter()

    door = Door(red_painter)
    wall = Wall(blue_painter)

    door.draw()
    wall.draw()