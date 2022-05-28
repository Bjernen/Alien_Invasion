import pygame
import sys

pygame.init()

size = width, height = 1200, 800
white = 255, 255, 255

screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            print(event.key)
    screen.fill(white)
    pygame.display.flip()