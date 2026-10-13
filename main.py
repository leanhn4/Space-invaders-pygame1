import pygame
from settings import *
from player import Player
from alien import Alien
from laser import Laser
from obstacle import create_obstacles
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
big_font = pygame.font.Font(None, 72)
player = Player()
player_lasers = pygame.sprite.Group()
alien_lasers = pygame.sprite.Group()
aliens = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
score = 0
game_over = False
def create_alien_wave():
    aliens.empty()
    for row in range(5):2  
    for column in range(10):
            x = 120 + column * 55
            y = 80 + row * 45
            alien = Alien(x, y, row)
            aliens.add(alien)
def reset_game():
    global score, game_over
    score = 0
    game_over = False
    player.reset()
    player_lasers.empty()
    alien_lasers.empty()
    obstacles.empty()
    obstacles.add(create_obstacles())
    create_alien_wave()
obstacles.add(create_obstacles())
create_alien_wave()
alien_direction = 1
alien_timer = 0
alien_shoot_timer = 0
running = True
while running:
    dt = clock.tick(FPS) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                player.shoot(player_lasers)
            if event.key == pygame.K_r and game_over:
                reset_game()
            if event.key == pygame.K_ESCAPE:
                running = False
    if not game_over:
        player.update()
        player_lasers.update()
        alien_lasers.update()
        # Move aliens as a formation.
        alien_timer += dt
        if alien_timer >= ALIEN_MOVE_INTERVAL:
            alien_timer = 0
            move_down = False
            for alien in aliens:
                alien.rect.x += ALIEN_MOVE_SPEED * alien_direction
                if (
                    alien.rect.right >= SCREEN_WIDTH - 20
                    or alien.rect.left <= 20
                ):
                    move_down = True
            if move_down:
                alien_direction *= -1
                for alien in aliens:
                    alien.rect.y += ALIEN_DROP_DISTANCE
        # Occasionally let a random alien fire.
        alien_shoot_timer += dt
        if alien_shoot_timer >= ALIEN_SHOOT_INTERVAL and aliens:
            alien_shoot_timer = 0
            shooter = list(aliens)[
                pygame.time.get_ticks() % len(aliens)
            ]
            alien_lasers.add(
                Laser(
                    shooter.rect.centerx,
                    shooter.rect.bottom,
                    1
                )
            )
        # Player laser vs aliens.
        for laser in list(player_lasers):
            hit = pygame.sprite.spritecollideany(
                laser,
                aliens
            )
            if hit:
                laser.kill()
                hit.kill()
                score += 10
        # Laser collisions with obstacles.
        for laser in list(player_lasers) + list(alien_lasers):
            pygame.sprite.spritecollide(
                laser,
                obstacles,
                True
            )
        # Alien lasers hitting player.
        if pygame.sprite.spritecollideany(
            player,
            alien_lasers
        ):
            game_over = True
        # Aliens reaching the player area.
        if any(
            alien.rect.bottom >= player.rect.top
            for alien in aliens
        ):
            game_over = True
        # New wave.
        if not aliens:
            create_alien_wave()
    screen.fill(BACKGROUND)
    obstacles.draw(screen)
    aliens.draw(screen)
    player_lasers.draw(screen)
    alien_lasers.draw(screen)
    screen.blit(
        player.image,
        player.rect
    )
    score_text = font.render(
        f"Score: {score}",
        True,
        TEXT
    )
    screen.blit(
        score_text,
        (20, 15)
    )
    controls = font.render(
        "Arrow keys / A-D to move   SPACE to shoot",
        True,
        TEXT
    )
    screen.blit(
        controls,
        (20, SCREEN_HEIGHT - 35)
    )
    if game_over:
        title = big_font.render(
            "GAME OVER",
            True,
            TEXT
        )
        restart = font.render(
            "Press R to restart or ESC to quit",
            True,
            TEXT
        )
        screen.blit(
            title,
            title.get_rect(
                center=(
                    SCREEN_WIDTH // 2,
                    SCREEN_HEIGHT // 2 - 30
                )
            )
        )
        screen.blit(
            restart,
            restart.get_rect(
                center=(
                    SCREEN_WIDTH // 2,
                    SCREEN_HEIGHT // 2 + 35
                )
            )
        )
    pygame.display.flip()
pygame.quit()
