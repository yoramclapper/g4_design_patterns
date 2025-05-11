from abc import ABC, abstractmethod
from enum import Enum
from typing import Optional
from spells import Spell


class Direction(Enum):
    NORTH = 'North'
    SOUTH = 'South'
    EAST = 'East'
    WEST = 'West'


class MapSite(ABC):
    """
    Interface to represent maze components
    """

    @abstractmethod
    def enter(self):
        """
        Shows what happens when entering maze component
        """
        pass


class Room(MapSite):
    def __init__(self, room_no: int):
        self._room_number: int = room_no
        self._sides: dict[Direction, Optional[MapSite]] = {
            Direction.NORTH: None,
            Direction.SOUTH: None,
            Direction.EAST: None,
            Direction.WEST: None
        }

    @property
    def room_number(self) -> int:
        return self._room_number

    @room_number.setter
    def room_number(self, room_no: int):
        self._room_number = room_no

    def enter(self):
        print(f"Entered room number {self._room_number}")

    def set_side(self, direction: Direction, map_site: MapSite):
        self._sides[direction] = map_site

    def get_side(self, direction: Direction) -> Optional[MapSite]:
        return self._sides[direction]


class EnchantedRoom(Room):

    def __init__(self, room_no: int, cast_spell: Spell):
        super().__init__(room_no)
        self._cast_spell = cast_spell

    def enter(self):
        print(f"Entered room number {self._room_number} enchanted with spell: {self._cast_spell.spell_name}")


class Wall(MapSite):

    def enter(self):
        print("Hit upon a wall")


class Door(MapSite):

    def __init__(self, room1: Room, room2: Room):
        self._room1: Room = room1
        self._room2: Room = room2
        self._is_open: Optional[bool] = None


    def set_room1(self, room: Room):
        self._room1 = room

    def set_room2(self, room: Room):
        self._room2 = room

    def enter(self):
        if self._is_open is None:
            print("Door not properly initialized unknown if open or closed")
        elif self._is_open:
            print("Entered open door")
        else:
            print("Hit upon closed door")

    def other_side_from_room(self, room: Room) -> Room:
        if room == self._room1:
            return self._room2
        elif room == self._room2:
            return self._room1
        else:
            print("Room not connected to door")


class DoorNeedingSpell(Door):

    def __init__(self, room1: Room, room2: Room):
        super().__init__(room1, room2)
        self._is_open = False

    def cast_spell(self, casted_spell: Spell):
        if casted_spell.spell_name == "Abracadabra":
            self._is_open = True
