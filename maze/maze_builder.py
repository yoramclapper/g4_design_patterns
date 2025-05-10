from abc import ABC, abstractmethod
from maze_game import Maze
from map_site import Direction, Room, Wall, Door


class MazeBuilder(ABC):
    """
    Abstract builder for maze components.
    """

    @abstractmethod
    def build_maze(self):
        """
        Builds a maze.
        """
        pass

    @abstractmethod
    def build_room(self, n: int):
        """
        Builds a room with the given room number.
        """
        pass

    @abstractmethod
    def build_door(self, n1: int, n2: int):
        """
        Builds a door between two rooms.
        """
        pass

    @abstractmethod
    def get_maze(self):
        """
        Returns the constructed maze.
        """
        pass


class StandardMazeBuilder(MazeBuilder):

    def __init__(self):
        self._current_maze = self.build_maze()

    @staticmethod
    def _common_wall() -> Direction:
        return Direction.NORTH

    def build_maze(self) -> Maze:
        return Maze()

    @property
    def get_maze(self):
        return self._current_maze

    def build_room(self, n: int):
        if self._current_maze:
            room = Room(room_no=n)
            room.set_side(direction=Direction.NORTH, map_site=Wall())
            room.set_side(direction=Direction.SOUTH, map_site=Wall())
            room.set_side(direction=Direction.EAST, map_site=Wall())
            room.set_side(direction=Direction.WEST, map_site=Wall())
            self._current_maze.add_room(room=room)

    def build_door(self, n1: int, n2: int):
        rooms = [None, None]
        for item in self._current_maze.rooms_in_maze:
            if item.room_number == n1:
                rooms[0] = item
            elif item.room_number == n2:
                rooms[1] = item
        if rooms[0] is None or rooms[1] is None:
            print("Rooms not found in maze")
        else:
            room1 = rooms[0]
            room2 = rooms[1]
            door = Door(room1=room1, room2=room2)
            room1.set_side(self._common_wall(), door)
            room2.set_side(self._common_wall(), door)


class MazeGame:
    """
    Creates maze using the builder pattern.
    """

    def __init__(self, builder: MazeBuilder):
        self._builder = builder

    def create_maze(self) -> Maze:
        """
        Constructs the maze using the builder.
        """

        self._builder.build_maze()
        self._builder.build_room(1)
        self._builder.build_room(2)
        self._builder.build_door(1, 2)

        return self._builder.get_maze






