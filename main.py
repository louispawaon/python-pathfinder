#Library Declaration
import pygame
import random
import time

#Variable Declaration
width, height = 1600, 900
icon = pygame.image.load('maze.png')
color_GREEN = (178,255,102)
color_PURPLE = (178,102,255)
color_WHITE = (225,225,225)
color_BLACK = (0,0,0)
color_RED = (255,21,21)
fps = 30
timer = pygame.time.Clock()
running = True

#Pygame Initialization
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Pathfinder Visualizer")
window = pygame.display.set_mode((width, height))
window.fill(color_WHITE)
pygame.display.set_icon(icon)

#Maze Elements
cell_width = 40
x=0
y=0

grid=[]
stack=[]
closed=[]

path={}

#Grid 
def build_grid(x,y,cell_width):
    for j in range (20):
        x=40
        y=y+40
        print (x,y)
        for h in range (40):
            pygame.draw.line(window, color_BLACK, [x + cell_width, y], [x + cell_width, y + cell_width], 2) # East wall
            pygame.draw.line(window, color_BLACK, [x , y], [x, y + cell_width], 2) # West wall
            pygame.draw.line(window, color_BLACK, [x, y], [x + cell_width, y], 2) # North wall
            pygame.draw.line(window, color_BLACK, [x, y + cell_width], [x + cell_width, y + cell_width], 2) # South wall

            grid.append((x,y))
            
            x=x+40
            pygame.display.update()
    print(grid)
x, y = 40, 40
build_grid(x,y,cell_width)

#Pygame Loop Logic
while running:
    timer.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

