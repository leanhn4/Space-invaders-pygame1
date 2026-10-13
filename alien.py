import pygame
from settings import *
class Alien(pygame.sprite.Sprite):
    def __init__(self, x, y, row):
        super().__init__()
        self.image = pygame.Surface(
            ALIEN_SIZE,
            pygame.SRCALPHA
        )
        if row == 0:
            color = (240, 90, 90)
        elif row < 3:
            color = (100, 180, 255)
        else:
            color = (190, 120, 240)
        pygame.draw.rect(
            self.image,
            color,
            (
                3,
                5,
                ALIEN_SIZE[0] - 6,
                ALIEN_SIZE[1] - 8
            ),
            border_radius=5
        )
        pygame.draw.circle(
            self.image,
            BACKGROUND,
            (11, 12),
            3
        )
        pygame.draw.circle(
            self.image,
            BACKGROUND,
            (23, 12),
            3
        )
        self.rect = self.image.get_rect(
            topleft=(x, y)
        )

