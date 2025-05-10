import maze_game
import maze_factory
import maze_builder

if __name__ == '__main__':
    maze_game.MazeGame.create_maze()
    maze_factory.MazeGame(maze_factory.BaseMazeFactory()).create_maze()
    maze_factory.MazeGame(maze_factory.EnchantedMazeFactory()).create_maze()
    maze_builder.MazeGame(maze_builder.StandardMazeBuilder()).create_maze()

