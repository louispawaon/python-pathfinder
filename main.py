#Library Declaration
import pygame
import random
import time

#Variable Declaration
width, height = 1280, 780
running = True
icon = pygame.image.load('maze.png')
color_GREEN = (178,255,102)
color_PURPLE = (178,102,255)
color_WHITE = (225,225,225)
color_BLACK = (0,0,255)
color_RED = (255,21,21)
fps = 30
timer = pygame.time.Clock()
cell_width = 40
x=0
y=0

grid=[]
stack=[]
closed=[]
path={}

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Pathfinder Visualizer")
window = pygame.display.set_mode((width, height))
window.fill(color_WHITE)
pygame.display.set_icon(icon)


#Grid 
def gen_grid(x,y,cell_width=cell_width):
    for x in range (20):
        x=40
        y=y+40
        for y in range (40):
            pygame.draw.line(window, color_BLACK, [x + cell_width, y], [x + cell_width, y + cell_width], 2) # East wall
            pygame.draw.line(window, color_BLACK,  [x , y], [x, y + cell_width], 2) # West wall
            pygame.draw.line(window, color_BLACK,  [x, y], [x + cell_width, y], 2) # North wall
            pygame.draw.line(window, color_BLACK,  [x, y + cell_width], [x + cell_width, y + cell_width], 2) # South wall

            grid.append((x,y))
            x=x+40

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

x,y = 40,40
gen_grid(40,0,40)