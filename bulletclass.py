import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, yo):
        super().__init__()
        self.screen = yo.screen
        self.color = (0, 128, 64)
        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, 6, 8)
        self.rect.midright = yo.rect.midright

        # Store the bullet's position as a decimal value.
        self.x = float(self.rect.x)

    def update(self):
        self.x += 1
        # Update the rect position.
        self.rect.x = self.x
        # print(self.rect.x)

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)