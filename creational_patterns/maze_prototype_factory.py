from copy import deepcopy
from maze_abstract_factory import AbstractMazeFactory
from map_site import Wall, Room, Door, Direction
from maze_game import Maze


class MazePrototypeFactory(AbstractMazeFactory):
    """
    A factory that creates creational_patterns components based on prototypes.
    """

    def __init__(self, maze: Maze, wall: Wall, room: Room, door: Door):
        self._prototype_maze = maze
        self._prototype_wall = wall
        self._prototype_room = room
        self._prototype_door = door

    def make_maze(self) -> Maze:
        return deepcopy(self._prototype_maze)

    def make_wall(self) -> Wall:
        return deepcopy(self._prototype_wall)

    def make_room(self, n: int) -> Room:
        room = deepcopy(self._prototype_room)
        room.room_number = n
        return room

    def make_door(self, r1: Room, r2: Room) -> Door:
        door = deepcopy(self._prototype_door)
        door.set_room1(room=r1)
        door.set_room1(room=r2)
        return door


class MazeGame:
    """
    Creates creational_patterns using prototype factory
    """

    def __init__(self, factory: MazePrototypeFactory):
        self._factory = factory

    def create_maze(self) -> Maze:
        maze = self._factory.make_maze()
        room1 = self._factory.make_room(1)
        room2 = self._factory.make_room(2)
        door = self._factory.make_door(room1, room2)

        room1.set_side(direction=Direction.NORTH, map_site=self._factory.make_wall())
        room1.set_side(direction=Direction.SOUTH, map_site=door)
        room1.set_side(direction=Direction.EAST, map_site=self._factory.make_wall())
        room1.set_side(direction=Direction.WEST, map_site=self._factory.make_wall())

        room2.set_side(direction=Direction.NORTH, map_site=self._factory.make_wall())
        room2.set_side(direction=Direction.SOUTH, map_site=self._factory.make_wall())
        room2.set_side(direction=Direction.EAST, map_site=self._factory.make_wall())
        room2.set_side(direction=Direction.WEST, map_site=door)

        maze.add_room(room1)
        maze.add_room(room2)

        return maze

