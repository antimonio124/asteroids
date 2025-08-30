from constants import SHOT_RADIUS
from circleshape import CircleShape
import pygame



class Shot(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2()
        
    def draw(self, surface):
        center = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(surface, "white", center, SHOT_RADIUS, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        
