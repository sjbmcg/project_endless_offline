# class + the game's loop
import pygame 
from src.setting import WINDOW_HEIGHT, WINDOW_WIDTH, FPS, BACKGROUND_COLOUR
from src.character import Character

class Game:
    def __init__(self, width, height, fps, background_color):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Endless Offline")
        self.clock = pygame.time.Clock()
        self.running = False
        # character's position (default rn)
        self.character = Character(10, 10)  # Starting at grid position (10, 10)
    
    def run(self):
        pygame.init()  # Initialize pygame
       
        texture_paths = {
            'standing': 'data/gfx/gfx008/101.png',
            'walking': 'data/gfx/gfx008/102.png',
            'sitting': 'data/gfx/gfx008/106.png'
        }
        self.character.load_textures(texture_paths)
        
        self.running = True

        while self.running:
            dt = self.clock.tick(FPS) / 1000.0  # Delta time in seconds
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            keys = pygame.key.get_pressed()  # Get current key states
            self.character.update(dt, keys)  # Update character with dt and keys
            
            self.screen.fill(BACKGROUND_COLOUR)
            self.character.render(self.screen)
            pygame.display.flip()