from map_site import Room, Door, Wall, Direction
from typing import Optional


class Maze:

    def __init__(self):
        self.rooms_in_maze: set[Optional[Room]] = set()

    def add_room(self, room: Room):
        self.rooms_in_maze.add(room)


class MazeGame:

    @staticmethod
    def create_maze() -> Maze:
        maze = Maze()

        r1 = Room(room_no=1)
        r2 = Room(room_no=2)
        door = Door(room1=r1, room2=r2)

        r1.set_side(direction=Direction.NORTH, map_site=Wall())
        r1.set_side(direction=Direction.SOUTH, map_site=door)
        r1.set_side(direction=Direction.EAST, map_site=Wall())
        r1.set_side(direction=Direction.WEST, map_site=Wall())

        r2.set_side(direction=Direction.NORTH, map_site=Wall())
        r2.set_side(direction=Direction.SOUTH, map_site=Wall())
        r2.set_side(direction=Direction.EAST, map_site=Wall())
        r2.set_side(direction=Direction.WEST, map_site=door)

        maze.add_room(room=r1)
        maze.add_room(room=r2)

        return maze
