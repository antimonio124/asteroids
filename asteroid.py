import pygame
import random
from circleshape import CircleShape
from constants import *
class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        

    def draw(self, surface):
        center = (self.position.x, self.position.y)
        pygame.draw.circle(surface, "white", center, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        pos = self.position.copy()
        vel = self.velocity
        r = self.radius
        new_radius = r - ASTEROID_MIN_RADIUS
        self.kill()

        if r <= ASTEROID_MIN_RADIUS:
            return

        
        random_angle = random.uniform(20, 50)
        vector1 = vel.rotate(random_angle) * 1.2
        vector2 = vel.rotate(-random_angle) * 1.2

        asteroid1 = Asteroid(pos.x, pos.y, new_radius)
        asteroid2 = Asteroid(pos.x, pos.y, new_radius)
        

        asteroid1.velocity = vector1 
        asteroid2.velocity = vector2 
