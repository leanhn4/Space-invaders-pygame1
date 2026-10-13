import pygame
from settings import *
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface(
            PLAYER_SIZE,
            pygame.SRCALPHA
        )
        pygame.draw.polygon(
            self.image,
            (80, 220, 120),
            [
                (PLAYER_SIZE[0] // 2, 0),
                (0, PLAYER_SIZE[1]),
                (PLAYER_SIZE[0], PLAYER_SIZE[1]),
            ],
        )
        self.rect = self.image.get_rect(
            midbottom=(
                SCREEN_WIDTH // 2,
                SCREEN_HEIGHT - 60
            )
        )
        self.last_shot = 0
        self.shoot_delay = 0.35
    def reset(self):
        self.rect.midbottom = (
            SCREEN_WIDTH // 2,
            SCREEN_HEIGHT - 60
        )
    def update(self):
        keys = pygame.key.get_pressed()
        direction = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            direction -= 1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            direction += 1
        self.rect.x += int(
            direction * PLAYER_SPEED / FPS
        )
        self.rect.left = max(
            self.rect.left,
            10
        )
        self.rect.right = min(
            self.rect.right,
            SCREEN_WIDTH - 10
        )
        self.last_shot = max(
            0,
            self.last_shot - 1 / FPS
        )
    def shoot(self, group):
        if self.last_shot <= 0:
            group.add(
                Laser(
                    self.rect.centerx,
                    self.rect.top,
                    -1
                )
            )
            self.last_shot = self.shoot_delay
from laser import Laser

