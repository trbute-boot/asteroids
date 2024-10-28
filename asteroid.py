import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        splitAngle = random.uniform(20, 50)
        velOne = self.velocity.rotate(splitAngle) * 1.2
        velTwo = self.velocity.rotate(-splitAngle) * 1.2
        newRadius = self.radius - ASTEROID_MIN_RADIUS
        fragmentOne = Asteroid(self.position.x, self.position.y, newRadius)
        fragmentOne.velocity = velOne
        fragmentTwo = Asteroid(self.position.x, self.position.y, newRadius)
        fragmentTwo.velocity = velTwo
