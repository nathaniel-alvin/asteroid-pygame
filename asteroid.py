import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "green", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        # check if its the smallest asteroid
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # generate a random angle
        new_angle = random.uniform(20, 50)
        new_vector_1 = self.velocity.rotate(new_angle)
        new_vector_2 = self.velocity.rotate(-new_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # create two new asteroids
        a_1 = Asteroid(self.position.x, self.position.y, new_radius)
        a_1.velocity = new_vector_1 * 1.2
        a_2 = Asteroid(self.position.x, self.position.y, new_radius)
        a_2.velocity = new_vector_2 * 1.2
