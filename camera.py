from abc import ABC, abstractmethod
import pygame
vec = pygame.math.Vector2


class Camera:
    def __init__(self, dis, surface):
        self.surface = surface
        self.dis = dis
        self.x = 0
        self.y = 0

    def update(self, count, running):
        if running:
            self.dis.blit(self.surface, (0 - (count + 0.5), 0))
            self.x = 0 - (count + 0.5)
            self.y = 0
        else:
            self.dis.blit(self.surface, (0 - (count + 1), 0))
            self.x = 0 - (count + 1)
            self.y = 0
