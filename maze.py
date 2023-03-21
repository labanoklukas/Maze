import pygame
import random
import time
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Maze Generator")
clock = pygame.time.Clock()

squares = []
visited = []
stack = []
fps = 60
orange = (255,0,122)
white = (255,255,255)
green = (0,0,255)
w = 20
x = 0
y = 0

def Squares(x, y, w):
    for i in range(1,21):
        x = 20
        y = y + 20
        for j in range(1, 21):
            pygame.draw.line(screen, white, [x, y], [x + w, y])
            pygame.draw.line(screen, white, [x + w, y], [x + w, y + w])
            pygame.draw.line(screen, white, [x + w, y + w], [x, y + w])
            pygame.draw.line(screen, white, [x, y + w], [x, y])
            squares.append((x, y))
            pygame.display.update()
            x = x + 20

def up(x, y):
    pygame.draw.rect(screen, orange, (x + 1, y - w + 1, 19, 39), 0)
    pygame.display.update()


def down(x, y):
    pygame.draw.rect(screen, orange, (x +  1, y + 1, 19, 39), 0)
    pygame.display.update()


def left(x, y):
    pygame.draw.rect(screen, orange, (x - w +1, y +1, 39, 19), 0)
    pygame.display.update()


def right(x, y):
    pygame.draw.rect(screen, orange, (x +1, y +1, 39, 19), 0)
    pygame.display.update()


def single_cell( x, y):
    pygame.draw.rect(screen, green, (x +1, y +1, 18, 18), 0)
    pygame.display.update()


def backtrack(x, y):
    pygame.draw.rect(screen, orange, (x +1, y +1, 18, 18), 0)
    pygame.display.update()

def makemaze(x, y):
    single_cell(x, y)
    stack.append((x, y))
    while len(stack) > 0:
        cell = []
        if (x + w, y) not in visited and (x + w, y) in squares:
            cell.append("right")

        if (x - w, y) not in visited and (x - w, y) in squares:
            cell.append("left")

        if (x , y + w) not in visited and (x , y + w) in squares:
            cell.append("down")

        if (x, y - w) not in visited and (x , y - w) in squares:
            cell.append("up")

        if len(cell) > 0:
            cell_chosen = (random.choice(cell))

            if cell_chosen == "right":
                right(x, y)
                x = x + w
                visited.append((x, y))
                stack.append((x, y))

            elif cell_chosen == "left":
                left(x, y)
                x = x - w
                visited.append((x, y))
                stack.append((x, y))

            elif cell_chosen == "down":
                down(x, y)
                y = y + w
                visited.append((x, y))
                stack.append((x, y))

            elif cell_chosen == "up":
                up(x, y)
                y = y - w
                visited.append((x, y))
                stack.append((x, y))
        else:
            x, y = stack.pop()

x,y =20,20
Squares(20, 0, 20)
makemaze(x, y)
Window = True
while Window:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Window = False
