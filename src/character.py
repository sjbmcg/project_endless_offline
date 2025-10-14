import pygame
from enum import Enum

class CharacterState(Enum):
    STANDING, WALKING, SITTING = 0, 1, 2

class Direction(Enum):
    DOWN, LEFT, UP, RIGHT = 0, 1, 2, 3

class Character:
    def __init__(self, x, y):
        # tryna think of a good pattern 

        # Character configurations 
        self.x = float(x)
        self.y = float(y)
        self.direction = Direction.DOWN
        self.state = CharacterState.STANDING
        self.gender = 0  
        self.skin = 0
        
        self.animation_frame = 0
        self.animation_timer = 0
        self.animation_speed = 200  
        self.speed = 3.0
        
        self.textures = {}
        self.dimensions = {
            'standing': (18, 58),
            'walking': (26, 61),
            'sitting': (24, 43)
        }

    def load_textures(self, texture_paths):
        for name, path in texture_paths.items():
            self.textures[name] = pygame.image.load(path).convert_alpha()

    def update(self, dt, keys):
        dx = 0
        dy = 0

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            dy -= 1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dy += 1
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx -= 1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx += 1

        if dx or dy:
            if abs(dx) > abs(dy):
                self.direction = Direction.RIGHT if dx > 0 else Direction.LEFT
            else:
                self.direction = Direction.DOWN if dy > 0 else Direction.UP

        if dx or dy:
            self.x += dx * self.speed * dt
            self.y += dy * self.speed * dt
            
            if self.state != CharacterState.SITTING:
                self.state = CharacterState.WALKING
        elif self.state == CharacterState.WALKING:
            self.state = CharacterState.STANDING

        if self.state == CharacterState.WALKING:
            self.animation_timer += dt * 1000
            if self.animation_timer >= self.animation_speed:
                self.animation_frame = (self.animation_frame + 1) % 4
                self.animation_timer = 0
        else:
            self.animation_frame = 0
            self.animation_timer = 0

    def get_iso_position(self):
        iso_x = (self.x - self.y) * 32
        iso_y = (self.x + self.y) * 16
        return iso_x, iso_y
    
    def get_sprite_rect(self):
        state_name = self.state.name.lower()
        w, h = self.dimensions[state_name]
        
        if self.state == CharacterState.STANDING:
            start_x = 0 if self.gender == 0 else w * 2
            source_x = start_x + (w if self.direction in [Direction.UP, Direction.LEFT] else 0)
        elif self.state == CharacterState.WALKING:
            start_x = 0 if self.gender == 0 else w * 8
            dir_offset = w * 4 if self.direction in [Direction.UP, Direction.LEFT] else 0
            source_x = start_x + dir_offset + w * self.animation_frame
        else:  # sitting
            start_x = 0 if self.gender == 0 else w * 2
            source_x = start_x + (w if self.direction in [Direction.UP, Direction.LEFT] else 0)
        
        return (source_x, self.skin * h, w, h)
    
    def render(self, screen, camera_x, camera_y):
        state_name = self.state.name.lower()
        texture = self.textures.get(state_name)
        if not texture:
            return
            
        sprite_rect = self.get_sprite_rect()
        w, h = sprite_rect[2], sprite_rect[3]
        
        sprite = pygame.Surface((w, h), pygame.SRCALPHA)
        sprite.blit(texture, (0, 0), sprite_rect)
        
        if self.direction in (Direction.RIGHT, Direction.UP):
            sprite = pygame.transform.flip(sprite, True, False)
        
        iso_x, iso_y = self.get_iso_position()

        screen_x = int(camera_x + iso_x - w // 2)
        screen_y = int(camera_y + iso_y - h)
        
        screen.blit(sprite, (screen_x, screen_y))