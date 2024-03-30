import pygame, sys
import numpy as np 
#-----importar constst---
from constants import *
# ----- PYGAME SETUP Inicio-----
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Tic Tac Toe AI')
screen.fill(BG_COLOR)
#----Clases---
class Borad:
   #----Inicio de Dibujo del tablero llamado "board"------
   def __init__(self):
       self.square = np.zeros((BOARD_ROWS, BOARD_COLS))
       self.empty_sqr = self.square #[square]
       self.marked_sqrs = 0

   def final_state(self):
      '''
         @return 0 if there is no win yet
         @return 1 if player 1 wins
         @return 2 if player 2 wins
      '''
      # vertical gana
      for col in range(BOARD_COLS):
         if self.square[0][col]== self.square[1][col] == self.square[2][col] != 0:
            return self.square[0][col]

      # horizontal gana
      for row in range(BOARD_ROWS):
         if self.square[row][0]== self.square[row][1] == self.square[row][2] != 0:
            return self.square[row][0]

      #desc diagonal
      if self.square[0][0] == self.square[1][1] == self.square[2][2] != 0:
         return self.square[1][1]

      #asc diagonal
      if self.square[2][0] == self.square[1][1] == self.square[0][2] != 0:
         return self.square[1][1]
      
      # no gano   
      return 0
   #-Esta disponible el cuadro del medio-
   def mark_sqr(self, row, col, player):
    self.square[row][col] = player
    self.marked_sqrs +=1

   def empty_sqr(self, row, col):
      return self.square[row][col] == 0

   def get_empty_sqrs(self):
      empty_sqrs = []
      for row in range(BOARD_ROWS):
         for col in range(BOARD_COLS):
            if self.empty_sqr(row,col):
               empty_sqrs.append((row, col))
      return empty_sqrs

   def isfull(self):
      return self.marked_sqrs == 9

   def isempty(self):
      return self.marked_sqrs == 0
class Game:
   def __init__(self):
       self.show_lines()
       self.board = Borad()
       # self.ai = AI()
       self.player = 1 #1 - X #2 - O
       self.gamemode = 'pvp' #pvp o ai
       self.running = True
       self.show_lines()
#---Dibujar Lineas---
   def show_lines(self):
      #VERTIAL
       pygame.draw.line(screen, LINE_COLOR,(SQSIZE,0),(SQSIZE,HEIGHT),LINE_WIDTH)
       pygame.draw.line(screen, LINE_COLOR,(WIDTH - SQSIZE,0),(WIDTH - SQSIZE,HEIGHT),LINE_WIDTH)   
      #HORIZONTAL
       pygame.draw.line(screen, LINE_COLOR,(0,SQSIZE),(WIDTH, SQSIZE),LINE_WIDTH)
       pygame.draw.line(screen, LINE_COLOR,(0, HEIGHT - SQSIZE),(WIDTH,HEIGHT - SQSIZE),LINE_WIDTH)
   def draw_fig(self, row, col):
      if self.player == 1:
         #Dibujo X
         # desc Linea
         start_desc = (col * SQSIZE + OFFSET, row * SQSIZE + OFFSET)
         end_desc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + SQSIZE - OFFSET)
         pygame.draw.line(screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)
         #asc Linestart_desc = (col * SQSIZE + OFFSET, row * SQSIZE + OFFSET)
         start_asc = (col * SQSIZE + OFFSET, row * SQSIZE + SQSIZE - OFFSET)
         end_asc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + OFFSET)
         pygame.draw.line(screen, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH)
         
      elif self.player == 2:
         #Dibujo O
         center =(col * SQSIZE + SQSIZE //2, row * SQSIZE + SQSIZE //2)
         pygame.draw.circle(screen, CIRC_COLOR, center, RADIUS, CIRC_WIDTH)
   def next_turn(self):
      self.player = self.player % 2 + 1
#---Main Total---
def main():
   #object
   game = Game()
   board = game.board
#---MainLoop----
   while True:
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
         if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            row = pos[1] // SQSIZE
            col = pos[0] // SQSIZE
            if board.empty_sqr(row, col):
               board.mark_sqr(row, col,game.player)
               game.draw_fig(row,col)
               game.next_turn()
         pygame.display.update()
main()
