import pygame


class Player:
    def __init__(self, screen):
        self.screen = screen
        pygame.draw.circle(self.screen, (0, 0, 0), (0, 0), 50)
