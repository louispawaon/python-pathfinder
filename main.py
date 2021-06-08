import pygame
import random
import time

width, height = 1280, 780
bg_color = (255,255,255)
running = True
icon = pygame.image.load('maze.png')

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Pathfinder Visualizer")
window = pygame.display.set_mode((width, height))
window.fill(bg_color)
pygame.display.set_icon(icon)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
