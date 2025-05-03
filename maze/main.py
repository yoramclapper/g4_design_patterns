import maze_game
import maze_factory

if __name__ == '__main__':
    maze_game.MazeGame.create_maze()
    maze_factory.MazeGame(maze_factory.BaseMazeFactory()).create_maze()

