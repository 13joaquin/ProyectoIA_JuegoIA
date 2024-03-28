#from asyncio import events
from ast import If
import sys
#from turtle import bgcolor, width
import pygame, sys
import numpy as np 

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
BOARD_ROWS = 3
BOARD_COLS =3

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Tic Tac Toe AI')
screen.fill(BG_COLOR)
#pygame.draw.line(screen,RED,(10,10),(300,300),10)

#board
board = np.zeros((BOARD_ROWS, BOARD_COLS))
#print(board)
#---Dibujar Lineas---
def draw_line():
    # 1 Horizontal
    pygame.draw.line(screen, LINE_COLOR,(0,200),(600,200),LINE_WIDTH)
    # 2 Horizontal
    pygame.draw.line(screen, LINE_COLOR,(0,400),(600,400),LINE_WIDTH)
    # 1 Vertical
    pygame.draw.line(screen, LINE_COLOR,(200,0),(200,600),LINE_WIDTH)
    # 2 Vertical
    pygame.draw.line(screen, LINE_COLOR,(400,0),(400,600),LINE_WIDTH)

#-Esta disponible el cuadro del medio-
def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == 0
def is_board_full():
    for row in range(BOARD_ROWS):
     for col in range(BOARD_COLS):
      if board[row][col] == 0:
        return False
    return True
#false
print(is_board_full())
#marking all squares
for row in range(BOARD_ROWS):
     for col in range(BOARD_COLS):
         mark_square(row,col,1)
#board total Full -true
print(is_board_full())
draw_line()
# ----MainLoop----
while True:
    for event in pygame.event.get():
     if event.type == pygame.QUIT:
         sys.exit()
    pygame.display.update()
