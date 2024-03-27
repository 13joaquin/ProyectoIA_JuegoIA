import pygame, sys
from pygame.locals import *
pygame.init()

DySPLAY = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello Wordl')

while True: #main game loop
    for evet in pygame.event.get():
     if evet.type ==quit:
       pygame.quit()
       sys.exit()
    pygame.displayx.update()