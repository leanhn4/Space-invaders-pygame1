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

Obstacle import pygame
from settings import *
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface(
            OBSTACLE_SIZE,
            pygame.SRCALPHA
        )
        pygame.draw.rect(
            self.image,
            (80, 190, 120),
            self.image.get_rect(),
            border_radius=8
        )
        # Cut-outs give the shield a simple arcade shape.
        pygame.draw.rect(
            self.image,
            BACKGROUND,
            (
                20,
                20,
                50,
                15
            )
        )
        self.rect = self.image.get_rect(
            midtop=(x, y)
        )
def create_obstacles():
    group = pygame.sprite.Group()
    positions = [
        SCREEN_WIDTH * 0.18,
        SCREEN_WIDTH * 0.39,
        SCREEN_WIDTH * 0.61,
        SCREEN_WIDTH * 0.82,
    ]
    for x in positions:
        group.add(
            Obstacle(
                int(x),
                SCREEN_HEIGHT - 150
            )
        )
    return group

