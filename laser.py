import pygame
from settings import *
class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.image = pygame.Surface(
            LASER_SIZE,
            pygame.SRCALPHA
        )
        pygame.draw.rect(
            self.image,
            (255, 240, 90),
            self.image.get_rect(),
            border_radius=2
        )
        self.rect = self.image.get_rect(
            center=(x, y)
        )
        self.direction = direction
    def update(self):
        self.rect.y += int(
            LASER_SPEED * self.direction / FPS
        )
        if (
            self.rect.bottom < 0
            or self.rect.top > SCREEN_HEIGHT
        ):
            self.kill ()

