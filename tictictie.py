#from asyncio import events
import sys
#from turtle import bgcolor, width
import pygame, sys

# ----- PYGAME SETUP-----
pygame.init()
#---- ALTURA PYGAME-----
WIDTH = 600
HEIGHT = 600
#----COLOR DEL FONDO----
BG_COLOR = (28,170,250)
#----OTRO COLOR-----
RED = (255,0,0)
LINE_COLOR = (23,145,135)
LINE_WIDTH = 15

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Tic Tac Toe AI')
screen.fill(BG_COLOR)
#pygame.draw.line(screen,RED,(10,10),(300,300),10)

def draw_line():
    # 1 Horizontal
    pygame.draw.line(screen, LINE_COLOR,(0,200),(600,200),LINE_WIDTH)
    # 2 Horizontal
    pygame.draw.line(screen, LINE_COLOR,(0,400),(600,400),LINE_WIDTH)
    # 1 Vertical
    pygame.draw.line(screen, LINE_COLOR,(200,0),(200,600),LINE_WIDTH)
    # 2 Vertical
    pygame.draw.line(screen, LINE_COLOR,(400,0),(400,600),LINE_WIDTH)
draw_line()
while True:
    for event in pygame.event.get():
     if event.type == pygame.QUIT:
         sys.exit()
    pygame.display.update()
