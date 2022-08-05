# Libraries
# from turtle import Screen
from pydantic import conset
import pygame
from regex import F
from camera import *
from map import *
from screens import *
from buttons import *
from player import *
# Constants
SPEED = 0.3
HIGH_SPEED = 0.6
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

# Variables
running = False


# Meta-game
pygame.init()
dis_width = SCREEN_WIDTH
dis_height = SCREEN_HEIGHT
dis = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.update()
pygame.display.set_caption('Stick Racing')
dis.fill((255, 255, 255))
screen = Screen()

# Screen Flags
screen.start_flag = False


# Map Creation
# surface = Map().surface
dis.blit(Map().surface, (0, 0))
print(Map().surfaceCoordinates)
Player(dis)

# Camera
camera = Camera(dis, Map().surface)

# Main Screen
game_over = False

count = 0
while not game_over:
    count += SPEED
    running = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        # if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        #     if screen.start_flag:
        #         # text detection
        #         if event.pos[0] > 759 and event.pos[0] < 959 and event.pos[1] > 203 and event.pos[1] < 253:
        #             print('Join')
        #             screen.join_flag = True
        #             screen.start_flag = False
        #             dis.blit(screen.join, (0, 0))

        #         if event.pos[0] > 759 and event.pos[0] < 959 and event.pos[1] > 325.48 and event.pos[1] < 375.48:
        #             print('Create')

        #         if event.pos[0] > 759 and event.pos[0] < 959 and event.pos[1] > 447.97 and event.pos[1] < 497.97:
        #             print('Exit')
        #             game_over = True

        #         if event.type == pygame.KEYDOWN:
        #             if event.key == pygame.K_RIGHT:
        #                 count += HIGH_SPEED
        #                 camera.update(count, True)
        #                 running = True
        #                 print('Right')
    if not running:
        count += SPEED
        camera.update(count, False)
        print('Left')
    print(camera.x, camera.y)
    Player(dis)
    pygame.display.update()


pygame.quit()
quit()
