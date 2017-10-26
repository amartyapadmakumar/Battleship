'''Input player names'''
player1=str(input("Player 1, enter your name:"))
player2=str(input("Player 2, enter your name:"))

'''Print Player 1's board'''
board1=[]
for i in range(10):
   z=['O']*10
   board1.append(z)

def print_board1(board):
   print(player1+':') 
   for i in board:
       print(" ".join(i))

print_board1(board1)

print()

'''Print Player 2's board'''
board2=[]
for i in range(10):
   z=['O']*10
   board2.append(z)

def print_board2(board):
   print(player2+':') 
   for i in board:
       print(" ".join(i))

print_board2(board2)

print()

def p1_hide_ships(board):
    accept_row_ship1=False
    accept_column_ship1=False
    accept_row_ship2=False
    accept_column_ship2=False
    accept_ship2=False
    accept_row_ship3=False
    accept_column_ship3=False
    accept_ship3=False
    accept_row_ship4=False
    accept_column_ship4=False
    accept_ship4=False
    accept_row_ship5=False
    accept_column_ship5=False
    accept_ship5=False
    
    while accept_row_ship1==False:
       row_ship1=input("%s, enter row where you want to hide Ship 1 (0-9):" % (player1))
       try:
          row_ship1=int(row_ship1)
       except ValueError:
          print("Input must be an integer")   
       if row_ship1 in range(10):
          accept_row_ship1=True
       else:
           print("Row must be in range 0-9")   
    while accept_column_ship1==False:      
       column_ship1=input('%s, enter column where you want to hide Ship 1 (0-9):'%(player1))
       try:
          column_ship1=int(column_ship1)
       except ValueError:
          print("Input must be an integer")   
       if column_ship1 in range(10):
          accept_column_ship1=True
       else:
          print("Column must be in range 0-9")   
    board[row_ship1][column_ship1]='S'

    while accept_ship2==False:
       while accept_row_ship2==False:
          row_ship2=input('%s, enter row where you want to hide Ship 2 (0-9):'%(player1))
          try:
             row_ship2=int(row_ship2)
          except ValueError:
             print("Input must be an integer")   
          if row_ship2 in range(10):
             accept_row_ship2=True
          else:
             print("Row must be in range 0-9")   
       while accept_column_ship2==False:      
          column_ship2=input('%s, enter column where you want to hide Ship 2 (0-9):'%(player1))
          try:
             column_ship2=int(column_ship2)
          except ValueError:
             print("Input must be an integer")   
          if column_ship2 in range(10):
             accept_column_ship2=True
          else:
             print("Column must be in range 0-9")   
       if board[row_ship2][column_ship2]=='O':    
          accept_ship2=True            
       elif board[row_ship2][column_ship2]=='S':
          print("You have already hid a ship in that location, please choose another location.")
          accept_row_ship2=False
          accept_column_ship2=False
    board[row_ship2][column_ship2]='S'

    while accept_ship3==False:
       while accept_row_ship3==False:
          row_ship3=input('%s, enter row where you want to hide Ship 3 (0-9):'%(player1))
          try:
             row_ship3=int(row_ship3)
          except ValueError:
             print("Input must be an integer")
          if row_ship3 in range(10):
             accept_row_ship3=True
          else:
             print("Row must be in range 0-9")   
       while accept_column_ship3==False:      
          column_ship3=input('%s, enter column where you want to hide Ship 3 (0-9):'%(player1))
          try:
             column_ship3=int(column_ship3)
          except ValueError:
             print("Input must be an integer")
          if column_ship3 in range(10):
             accept_column_ship3=True
          else:
             print("Column must be in range 0-9")   
       if board[row_ship3][column_ship3]=='O':    
          accept_ship3=True            
       elif board[row_ship3][column_ship3]=='S':
          print("You have already hid a ship in that location, please choose another location.")
          accept_row_ship3=False
          accept_column_ship3=False          
    board[row_ship3][column_ship3]='S'
    
    while accept_ship4==False:
       while accept_row_ship4==False:
          row_ship4=input('%s, enter row where you want to hide Ship 4 (0-9):'%(player1))
          try:
             row_ship4=int(row_ship4)
          except ValueError:
             print("Input must be an integer")
          if row_ship4 in range(10):
             accept_row_ship4=True
          else:
             print("Row must be in range 0-9")   
       while accept_column_ship4==False:      
          column_ship4=input('%s, enter column where you want to hide Ship 4 (0-9):'%(player1))
          try:
             column_ship4=int(column_ship4)
          except ValueError:
             print("Input must be an integer")
          if column_ship4 in range(10):
             accept_column_ship4=True
          else:
             print("Column must be in range 0-9")
       if board[row_ship4][column_ship4]=='O':    
          accept_ship4=True            
       elif board[row_ship4][column_ship4]=='S':
          print("You have already hid a ship in that location, please choose another location.")
          accept_row_ship4=False
          accept_column_ship4=False
    board[row_ship4][column_ship4]='S'

    while accept_ship5==False:
       while accept_row_ship5==False:
          row_ship5=input('%s, enter row where you want to hide Ship 5 (0-9):'%(player1))
          try:
             row_ship5=int(row_ship5)
          except ValueError:
             print("Input must be an integer")
          if row_ship5 in range(10):
             accept_row_ship5=True
          else:
             print("Row must be in range 0-9")
       while accept_column_ship5==False:      
          column_ship5=input('%s, enter column where you want to hide Ship 5 (0-9):'%(player1))
          try:
             column_ship5=int(column_ship5)
          except ValueError:
             print("Input must be an integer")
          if column_ship5 in range(10):
             accept_column_ship5=True
          else:
             print("Column must be in range 0-9")
       if board[row_ship5][column_ship5]=='O':    
          accept_ship5=True            
       elif board[row_ship5][column_ship5]=='S':
          print("You have already hid a ship in that location, please choose another location.")
          accept_row_ship5=False
          accept_column_ship5=False
    board[row_ship5][column_ship5]='S'

    print_board1(board)

p1_hide_ships(board1)

print()


def p2_hide_ships(board):
    accept_row_ship1=False
    accept_column_ship1=False
    accept_row_ship2=False
    accept_column_ship2=False
    accept_ship2=False
    accept_row_ship3=False
    accept_column_ship3=False
    accept_ship3=False
    accept_row_ship4=False
    accept_column_ship4=False
    accept_ship4=False
    accept_row_ship5=False
    accept_column_ship5=False
    accept_ship5=False
    
    while accept_row_ship1==False:
       row_ship1=input("%s, enter row where you want to hide Ship 1 (0-9):" % (player2))
       try:
          row_ship1=int(row_ship1)
       except ValueError:
          print("Input must be an integer")   
       if row_ship1 in range(10):
          accept_row_ship1=True
       else:
           print("Row must be in range 0-9")   
    while accept_column_ship1==False:      
       column_ship1=input('%s, enter column where you want to hide Ship 1 (0-9):'%(player2))
       try:
          column_ship1=int(column_ship1)
       except ValueError:
          print("Input must be an integer")   
       if column_ship1 in range(10):
          accept_column_ship1=True
       else:
          print("Column must be in range 0-9")   
    board[row_ship1][column_ship1]='S'

    while accept_ship2==False:
       while accept_row_ship2==False:
          row_ship2=input('%s, enter row where you want to hide Ship 2 (0-9):'%(player2))
          try:
             row_ship2=int(row_ship2)
          except ValueError:
             print("Input must be an integer")   
          if row_ship2 in range(10):
             accept_row_ship2=True
          else:
             print("Row must be in range 0-9")   
       while accept_column_ship2==False:      
          column_ship2=input('%s, enter column where you want to hide Ship 2 (0-9):'%(player2))
          try:
             column_ship2=int(column_ship2)
          except ValueError:
             print("Input must be an integer")   
          if column_ship2 in range(10):
             accept_column_ship2=True
          else:
             print("Column must be in range 0-9")   
       if board[row_ship2][column_ship2]=='O':    
          accept_ship2=True            
       elif board[row_ship2][column_ship2]=='S':
          print("You have already hid a ship in that location, please choose another location.")
          accept_row_ship2=False
          accept_column_ship2=False
    board[row_ship2][column_ship2]='S'

    while accept_ship3==False:
       while accept_row_ship3==False:
          row_ship3=input('%s, enter row where you want to hide Ship 3 (0-9):'%(player2))
          try:
             row_ship3=int(row_ship3)
          except ValueError:
             print("Input must be an integer")
          if row_ship3 in range(10):
             accept_row_ship3=True
          else:
             print("Row must be in range 0-9")   
       while accept_column_ship3==False:      
          column_ship3=input('%s, enter column where you want to hide Ship 3 (0-9):'%(player2))
          try:
             column_ship3=int(column_ship3)
          except ValueError:
             print("Input must be an integer")
          if column_ship3 in range(10):
             accept_column_ship3=True
          else:
             print("Column must be in range 0-9")   
       if board[row_ship3][column_ship3]=='O':    
          accept_ship3=True            
       elif board[row_ship3][column_ship3]=='S':
          print("You have already hid a ship in that location, please choose another location.")
          accept_row_ship3=False
          accept_column_ship3=False          
    board[row_ship3][column_ship3]='S'
    
    while accept_ship4==False:
       while accept_row_ship4==False:
          row_ship4=input('%s, enter row where you want to hide Ship 4 (0-9):'%(player2))
          try:
             row_ship4=int(row_ship4)
          except ValueError:
             print("Input must be an integer")
          if row_ship4 in range(10):
             accept_row_ship4=True
          else:
             print("Row must be in range 0-9")   
       while accept_column_ship4==False:      
          column_ship4=input('%s, enter column where you want to hide Ship 4 (0-9):'%(player2))
          try:
             column_ship4=int(column_ship4)
          except ValueError:
             print("Input must be an integer")
          if column_ship4 in range(10):
             accept_column_ship4=True
          else:
             print("Column must be in range 0-9")
       if board[row_ship4][column_ship4]=='O':    
          accept_ship4=True            
       elif board[row_ship4][column_ship4]=='S':
          print("You have already hid a ship in that location, please choose another location.")
          accept_row_ship4=False
          accept_column_ship4=False
    board[row_ship4][column_ship4]='S'

    while accept_ship5==False:
       while accept_row_ship5==False:
          row_ship5=input('%s, enter row where you want to hide Ship 5 (0-9):'%(player2))
          try:
             row_ship5=int(row_ship5)
          except ValueError:
             print("Input must be an integer")
          if row_ship5 in range(10):
             accept_row_ship5=True
          else:
             print("Row must be in range 0-9")
       while accept_column_ship5==False:      
          column_ship5=input('%s, enter column where you want to hide Ship 5 (0-9):'%(player2))
          try:
             column_ship5=int(column_ship5)
          except ValueError:
             print("Input must be an integer")
          if column_ship5 in range(10):
             accept_column_ship5=True
          else:
             print("Column must be in range 0-9")
       if board[row_ship5][column_ship5]=='O':    
          accept_ship5=True            
       elif board[row_ship5][column_ship5]=='S':
          print("You have already hid a ship in that location, please choose another location.")
          accept_row_ship5=False
          accept_column_ship5=False
    board[row_ship5][column_ship5]='S'

    print_board2(board)

p2_hide_ships(board2)

print()

def guess_ships():
   accept_guess_row=False
   accept_guess_col=False
   accept_guess=False
   player1_hit_count=0
   player2_hit_count=0
   while player1_hit_count<5 and player2_hit_count<5:
      while accept_guess==False:
         while accept_guess_row==False:
            p1_guess_row=input("%s, guess row of battleship (0-9):" % (player1))
            try:
               p1_guess_row=int(p1_guess_row)
            except ValueError:
               print("Input must be an integer")
            if p1_guess_row in range(10):
               accept_guess_row=True
            else:
               print("Row must be in range 0-9")
         while accept_guess_col==False:      
            p1_guess_col=input("%s, guess column of battleship (0-9):" % (player1))
            try:
               p1_guess_col=int(p1_guess_col)
            except ValueError:
               print("Input must be an integer")
            if p1_guess_col in range(10):
               accept_guess_col=True
            else:
               print("Column must be in range 0-9")                                  

         if board2[p1_guess_row][p1_guess_col]== 'X' or board2[p1_guess_row][p1_guess_col]== 'M':
            print ("You have already guessed in that location. Guess again")
            accept_guess_row=False
            accept_guess_col=False
         else:
            accept_guess=True
         
      if board2[p1_guess_row][p1_guess_col]== 'S' :
         print ("You sunk %s's battleship!" %(player2))
         board2[p1_guess_row][p1_guess_col]= 'X'                                        
         player1_hit_count+=1                       
      elif board2[p1_guess_row][p1_guess_col]== 'O' :
         print ("You missed.")                                
         board2[p1_guess_row][p1_guess_col]= 'M'

      accept_guess_row=False
      accept_guess_col=False
      accept_guess=False
                          
      while accept_guess==False:
         while accept_guess_row==False:
            p2_guess_row=input("%s, guess row of battleship (0-9):" % (player2))
            try:
               p2_guess_row=int(p2_guess_row)
            except ValueError:
               print("Input must be an integer")
            if p2_guess_row in range(10):
               accept_guess_row=True
            else:
               print("Row must be in range 0-9")
         while accept_guess_col==False:      
            p2_guess_col=input("%s, guess column of battleship (0-9):" % (player2))
            try:
               p2_guess_col=int(p2_guess_col)
            except ValueError:
               print("Input must be an integer")
            if p2_guess_col in range(10):
               accept_guess_col=True
            else:
               print("Column must be in range 0-9")                                  

         if board1[p2_guess_row][p2_guess_col]== 'X' or board1[p2_guess_row][p2_guess_col]== 'M':
            print ("You have already guessed in that location. Guess again")
            accept_guess_row=False
            accept_guess_col=False
         else:
            accept_guess=True
            
         
      if board1[p2_guess_row][p2_guess_col]== 'S' :
         print ("You sunk %s's battleship!" %(player1))
         board1[p2_guess_row][p2_guess_col]= 'X'                                         
         player2_hit_count+=1                       
      elif board1[p2_guess_row][p2_guess_col]== 'O' :
         print ("You missed.")
         board1[p2_guess_row][p2_guess_col]= 'M'                                   

      accept_guess_row=False
      accept_guess_col=False
      accept_guess=False

   print()

   if player1_hit_count > player2_hit_count:
      print("%s wins!"%(player1))
   elif player2_hit_count > player1_hit_count:
      print("%s wins!"%(player2))   
   else:
      print("Tie!")
      

guess_ships()

    
