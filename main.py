#Library Declaration
import pygame
import random
import time

#Variable Declaration
width, height = 1280, 780
icon = pygame.image.load('maze.png')
color_GREEN = (178,255,102)
color_PURPLE = (178,102,255)
color_WHITE = (225,225,225)
color_BLACK = (0,0,0)
color_RED = (255,21,21)
color_YELLOW =(255,255,102)
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
        for h in range (40):
            pygame.draw.line(window, color_BLACK, [x + cell_width, y], [x + cell_width, y + cell_width], 2) #Right Side
            pygame.draw.line(window, color_BLACK, [x , y], [x, y + cell_width], 2) #Left Side
            pygame.draw.line(window, color_BLACK, [x, y], [x + cell_width, y], 2) #Top Side
            pygame.draw.line(window, color_BLACK, [x, y + cell_width], [x + cell_width, y + cell_width], 2) #Bottom Side

            grid.append((x,y))
            x=x+40
            pygame.display.update()

#Movement Functions
def right_wall(x,y):
    pygame.draw.rect(window, color_GREEN,(y+1,y+1,79,39),0)
    pygame.display.update()

def left_wall(x,y):
    pygame.draw.rect(window, color_GREEN,(x-cell_width +1,y+1,79,39),0)
    pygame.display.update()

def top_wall(x,y):
    pygame.draw.rect(window, color_GREEN,(x+1,y-cell_width+1,39,39),0)
    pygame.display.update()

def bottom_wall(x,y):
    pygame.draw.rect(window, color_GREEN,(x+1,y+1,39,79),0)
    pygame.display.update()

def move_cell(x,y):
    pygame.draw.rect(window, color_PURPLE,(x+1,y+1,38,38),0)
    pygame.display.update()

def bactracker_cell(x,y):
    pygame.draw.rect(window, color_YELLOW,(x+1,y+1,38,38),0)
    pygame.display.update()

def path_tracker(x,y):
    pygame.draw.rect(window, color_RED,(x+1,y+1,16,16),0)
    pygame.display.update()

#Maze Algorithm Implementation
def maze_logic(x,y):
    move_cell(x,y)
    stack.append((x,y))
    closed.append((x,y))

    while len(stack)>0:
        time.sleep(0.1)
        cell=[]

        if(x+cell_width,y) not in closed and (x+cell_width,y)in grid:
            cell.append("East")
        
        

x, y = 40, 40
build_grid(x,y,cell_width)

#Pygame Loop Logic
while running:
    timer.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
#BFA, DFS, A* to implement 
