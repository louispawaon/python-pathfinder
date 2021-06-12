#Library Declaration
import pygame
import random
import time

#Variable Declaration
width, height = 500, 600
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
cell_width = 20
x=0
y=0

grid=[]
stack=[]
closed=[]

solution_path={}

#Grid 
def build_grid(x,y,cell_width):
    for j in range (20):
        x=20
        y=y+20
        for h in range (20):
            pygame.draw.line(window, color_BLACK, [x + cell_width, y], [x + cell_width, y + cell_width]) #Right Side
            pygame.draw.line(window, color_BLACK, [x, y + cell_width],[x , y]) #Left Side
            pygame.draw.line(window, color_BLACK, [x, y], [x + cell_width, y]) #Top Side
            pygame.draw.line(window, color_BLACK, [x + cell_width, y + cell_width],[x, y + cell_width]) #Bottom Side

            grid.append((x,y))
            x=x+20
            pygame.display.update()

#Movement Functions
def right_wall(x,y):
    pygame.draw.rect(window, color_GREEN,(y+1,y+1,39,19),0)
    pygame.display.update()

def left_wall(x,y):
    pygame.draw.rect(window, color_GREEN,(x-cell_width+1,y+1,39,19),0)
    pygame.display.update()

def top_wall(x,y):
    pygame.draw.rect(window, color_GREEN,(x+1,y-cell_width+1,19,39),0)
    pygame.display.update()

def bottom_wall(x,y):
    pygame.draw.rect(window, color_GREEN,(x+1,y+1,39,19),0)
    pygame.display.update()

def move_cell(x,y):
    pygame.draw.rect(window, color_PURPLE,(x+1,y+1,18,18),0)
    pygame.display.update()

def bactracker_cell(x,y):
    pygame.draw.rect(window, color_GREEN,(x+1,y+1,18,18),0)
    pygame.display.update()

def path_tracker(x,y):
    pygame.draw.rect(window, color_RED,(x+8,y+8,5,5),0)
    pygame.display.update()

#Maze Algorithm Implementation
def maze_logic(x,y):
    move_cell(x,y)
    stack.append((x,y))
    closed.append((x,y))

    while len(stack)>0:
        time.sleep(0.07)
        cell=[]

        if(x+cell_width,y) not in closed and (x+cell_width,y)in grid:
            cell.append("Right")

        if(x-cell_width,y) not in closed and (x-cell_width,y)in grid:
            cell.append("Left")

        if(x,y+cell_width) not in closed and (x,y+cell_width)in grid:
            cell.append("Bottom")
        
        if(x,y-cell_width) not in closed and (x,y-cell_width)in grid:
            cell.append("Top")

        if len(cell)>0:
            current_cell = (random.choice(cell))

            if (current_cell=="Right"):
                right_wall(x,y)
                solution_path[(x+cell_width,y)]=x,y
                x=x+cell_width
                closed.append((x,y))
                stack.append((x,y))

            elif (current_cell=="Left"):
                left_wall(x,y)
                solution_path[(x-cell_width,y)]=x,y
                x=x-cell_width
                closed.append((x,y))
                stack.append((x,y))

            elif (current_cell=="Top"):
                top_wall(x,y)
                solution_path[(x,y-cell_width)]=x,y
                y=y-cell_width
                closed.append((x,y))
                stack.append((x,y))

            elif (current_cell=="Bottom"):
                bottom_wall(x,y)
                solution_path[(x,y+cell_width)]=x,y
                y=y+cell_width
                closed.append((x,y))
                stack.append((x,y))

        else:
            x,y=stack.pop()
            move_cell(x,y)
            time.sleep(0.05)
            bactracker_cell(x,y)

def tracer(x,y):
    path_tracker(x,y)
    while(x,y)!=(20,20):
        x,y=solution_path[x,y]
        path_tracker(x, y)
        time.sleep(0.1)

x, y = 20, 20
build_grid(40,0,20)
maze_logic(x,y)
tracer(400,400)

#Pygame Loop Logic
while running:
    timer.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
#BFA, DFS, A* to implement 
