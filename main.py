import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # groups
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()

    Player.containers = (updatable_group, drawable_group)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroid_group, updatable_group, drawable_group)
    AsteroidField.containers = updatable_group
    _ = AsteroidField()

    Shot.containers = (shot_group, updatable_group, drawable_group)

    # game loop
    while True:
        # limit to 60 FPS
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for updatable in updatable_group:
            updatable.update(dt)

        for ast in asteroid_group:
            # check if any asteroid collide with player
            if ast.check_collision(player):
                print("Game over!")
                return
            for bullet in shot_group:
                if ast.check_collision(bullet):
                    ast.split()
                    bullet.kill()

        for drawable in drawable_group:
            drawable.draw(screen)

        # refresh/update screen
        pygame.display.flip()


if __name__ == "__main__":
    print("Starting asteroids!")
    main()
