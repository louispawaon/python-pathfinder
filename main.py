import pygame
import random
import time

width, height = 1920, 1080
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Pathfinder Visualizer")
window = pygame.display.set_mode((width, height))

pygame.display.update()
