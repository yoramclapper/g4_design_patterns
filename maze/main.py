import maze_game
import maze_abstract_factory
import maze_builder
import maze_prototype_factory
from map_site import Wall, Room, Door
from maze_game import Maze

if __name__ == '__main__':
    maze_game.MazeGame.create_maze()
    maze_abstract_factory.MazeGame(maze_abstract_factory.BaseMazeFactory()).create_maze()
    maze_abstract_factory.MazeGame(maze_abstract_factory.EnchantedMazeFactory()).create_maze()
    maze_builder.MazeGame(maze_builder.StandardMazeBuilder()).create_maze()

    maze_prototype_factory.MazeGame(
        maze_prototype_factory.MazePrototypeFactory(
            maze=maze_game.Maze(),
            wall=Wall(),
            room=Room(room_no=1),
            door=Door(room1=None, room2=None)
        )
    ).create_maze()
