#----OTRO COLOR-----
RED = (255,0,0)


CIRCLE_RADIUS = SQUARE_SIZE//3
CROSS_WIDTH = 25
CROSS_COLOR = (66, 66, 66)



#pygame.draw.line(screen,RED,(10,10),(300,300),10)

def draw_figures():
    for row in range(BOARD_ROWS):
       for col in range(BOARD_COLS):
          if board[row][col] == 1:
             pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE//2), int(row * SQUARE_SIZE + SQUARE_SIZE//2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
          elif board[row][col] == 2:
             pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)  
             pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)
          


def available_square(row, col):
    return board[row][col] == 0
def is_board_full():
    for row in range(BOARD_ROWS):
     for col in range(BOARD_COLS):
      if board[row][col] == 0:
        return False
    return True
#--Ganardor de lista----
def check_win(player):
   # vertical win check
   for col in range(BOARD_COLS):
      if board[0][col] == player and board[1][col] == player and board[2][col] == player:
         draw_vertical_winning_line(col, player)
         return True

   #horizontal win check
   for row in range(BOARD_ROWS):
      if board[row][0] == player and board[row][1] == player and board[row][2] == player:
         draw_horizontal_winning_line(row, player)
         return True 
      
   #asc diagonal win check
   if board[2][0] == player and board[1][1] == player and board[0][2] == player:
      draw_asc_diagonal(player)
      return True
   
   #desc diagonal win check
   if board[0][0] == player and board[1][1] == player and board[2][2] == player:
      draw_desc_diagonal(player)
      return True
   
   return False

def draw_vertical_winning_line(col, player):
   posX = col * SQUARE_SIZE + SQUARE_SIZE//2

   if player == 1:
      color = CIRCLE_COLOR
   elif player == 2:
      color = CROSS_COLOR

   pygame.draw.line(screen, color, (posX, 15), (posX, HEIGHT - 15), 15)      

def draw_horizontal_winning_line(row, player):
   posY = row * SQUARE_SIZE + SQUARE_SIZE//2

   if player == 1:
      color = CIRCLE_COLOR
   elif player == 2:
      color = CROSS_COLOR

   pygame.draw.line(screen, color, (15, posY), (WIDTH - 15, posY), 15)      

def draw_asc_diagonal(player):
   if player == 1:
      color = CIRCLE_COLOR
   elif player == 2:
      color = CROSS_COLOR

   pygame.draw.line(screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)   

def draw_desc_diagonal(player):
   if player == 1:
      color = CIRCLE_COLOR
   elif player == 2:
      color = CROSS_COLOR

   pygame.draw.line(screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), 15)   

#---Reiniciar partida----
def restart():
   screen.fill(BG_COLOR)
   draw_line()
   player = 1
   for row in range(BOARD_ROWS):
      for col in range(BOARD_COLS):
         board[row][col] = 0 

draw_line()
game_over = False
# ----MainLoop----

      and not game_over:
         mouseX = event.pos[0] #x
         mouseY = event.pos[1] #y
        
         clicked_row = int(mouseY // SQUARE_SIZE)
         clicked_col = int(mouseX // SQUARE_SIZE)

         if available_square(clicked_row, clicked_col):
             mark_square(clicked_row, clicked_col, player)
             if check_win(player):
                game_over = True
             player = player % 2 + 1

             draw_figures()
     if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_r:
           restart()
           game_over = False       
             
