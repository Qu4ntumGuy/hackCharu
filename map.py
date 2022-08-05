import pygame
import random


class Map:
    def __init__(self):
        self.surface = pygame.Surface((120000, 800))
        self.surfaceCoordinates = []
        self.random_map()

    def random_map(self):
        self.surface.fill((255, 255, 255))
        Length = 0
        for i in range(0, 120000, 100):

            Random_Height = random.randint(100, 400)
            Random_Width = random.randint(200, 800)
            Random_Gap = random.randint(50, 200)
            pygame.draw.rect(self.surface, (0, 0, 0),
                             (Length, 720 - Random_Height, Random_Width,  Random_Height), border_top_left_radius=5, border_top_right_radius=5)
            self.surfaceCoordinates.append(
                (Length, 720 - Random_Height, Random_Width,  Random_Height))

            Length += Random_Width + Random_Gap
