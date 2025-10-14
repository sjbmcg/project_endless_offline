import sys 
import pygame
# we'll create a game.py 
from src.game import Game
from src.setting import WINDOW_WIDTH, WINDOW_HEIGHT, FPS, BACKGROUND_COLOUR

def main():
    pygame.init()

    # let's assume that Game takes three parameters (height, width)
    game = Game(WINDOW_WIDTH, WINDOW_HEIGHT, FPS, BACKGROUND_COLOUR)
    game.run()


if __name__ == "__main__":
    sys.exit(main())