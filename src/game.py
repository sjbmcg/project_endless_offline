# class + the game's loop
import pygame 
from src.character import Character
from src.map_loader import MapLoader

class Game:
    def __init__(self, width, height, fps, background_color, character_texture_path):
        self.width = width
        self.height = height
        self.fps = fps
        self.background_color = background_color
        self.character_texture_path = character_texture_path
        self.screen = pygame.display.set_mode((self.width, self.height))
       
        pygame.display.set_caption("Endless Offline")
        self.clock = pygame.time.Clock()
        self.running = False
        # character's position (default rn)
        self.character = Character(0, 0)  # Starting at grid position (10, 10)
        self.map_loader = MapLoader()
    
    def run(self):
        pygame.init()  
       
        self.character.load_textures(self.character_texture_path)
        
        self.running = True

        while self.running:
            dt = self.clock.tick(self.fps) / 1000.0  # Delta time in seconds
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            keys = pygame.key.get_pressed()  # Get current key states
            self.character.update(dt, keys)  # Update character with dt and keys
            
            self.screen.fill(self.background_color)
            # think i should call this camera tbh
            camera_x = self.width // 2
            camera_y = self.height // 2
            self.character.render(self.screen, camera_x, camera_y)
            self.map_loader.load_emf("data/maps/00005.emf") # have't got the map yet importing it over 
            pygame.display.flip()