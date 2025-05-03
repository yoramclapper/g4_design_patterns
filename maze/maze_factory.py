from abc import ABC, abstractmethod
from maze_game import Maze
from map_site import Room, Wall, Door, Direction


class AbstractMazeFactory(ABC):

    @abstractmethod
    def make_maze(self) -> Maze:
        pass

    @abstractmethod
    def make_wall(self) -> Wall:
        pass

    @abstractmethod
    def make_room(self, n: int) -> Room:
        pass

    @abstractmethod
    def make_door(self, r1: Room, r2: Room) -> Door:
        pass


class BaseMazeFactory(AbstractMazeFactory):

    def make_maze(self) -> Maze:
        return Maze()

    def make_wall(self) -> Wall:
        return Wall()

    def make_room(self, n: int) -> Room:
        return Room(room_no=n)

    def make_door(self, r1: Room, r2: Room):
        return Door(room1=r1, room2=r2)


class MazeGame:
    """
    Creates maze with abstract factory method
    """

    def __init__(self, factory: AbstractMazeFactory):
        self._factory = factory

    def create_maze(self) -> Maze:
        maze = self._factory.make_maze()

        r1 = self._factory.make_room(n=1)
        r2 = self._factory.make_room(n=2)
        door = self._factory.make_door(r1=r1, r2=r2)

        r1.set_side(direction=Direction.NORTH, map_site=self._factory.make_wall())
        r1.set_side(direction=Direction.SOUTH, map_site=door)
        r1.set_side(direction=Direction.EAST, map_site=self._factory.make_wall())
        r1.set_side(direction=Direction.WEST, map_site=self._factory.make_wall())

        r2.set_side(direction=Direction.NORTH, map_site=self._factory.make_wall())
        r2.set_side(direction=Direction.SOUTH, map_site=self._factory.make_wall())
        r2.set_side(direction=Direction.EAST, map_site=self._factory.make_wall())
        r2.set_side(direction=Direction.WEST, map_site=door)

        maze.add_room(room=r1)
        maze.add_room(room=r2)

        return maze
