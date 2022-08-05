import pygame
import random


class Screen:
    def __init__(self):
        self.start = pygame.Surface((1080, 720))
        self.join = pygame.Surface((1080, 720))
        self.join_flag = False
        self.start_flag = False
        self.start_screen()
        self.join_screen()

    def start_screen(self):
        self.start.fill((255, 255, 255))
        font_Rect = pygame.font.SysFont('GothamMedium.ttf', 40)
        # font_Rect.set_bold(True)
        # font_Rect.set_underline(True)
        text_Start = font_Rect.render('Join', True, (0, 0, 0))
        text_Create = font_Rect.render('Create', True, (0, 0, 0))
        text_Exit = font_Rect.render('Exit', True, (0, 0, 0))
        self.start.blit(text_Start, (759,  203))
        self.start.blit(text_Create, (759,  325.48))

        self.start.blit(text_Exit, (759, 447.97))
        pygame.display.update()

    def join_screen(self):
        self.join.fill((255, 255, 255))
        font_Rect = pygame.font.SysFont('GothamMedium.ttf', 40)
        text_Start = font_Rect.render('Join', True, (0, 0, 0))

        self.join.blit(text_Start, (759,  203))

        pygame.display.update()
