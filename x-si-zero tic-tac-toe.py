from random import randrange


board = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]
]

def display_board(board):
  # The function accepts one parameter containing the board's current status
  # and prints it out to the console.
  
  # print("+-------"*3+"+")
  # print("|       "*3+"|")    
  # print("|   ",board[0][0],"   |   ",board[0][1],"   |   ",board[0][2],"   |", sep="")
  # print("|       "*3+"|")
  # print("+-------"*3+"+")
  # print("|       "*3+"|")    
  # print("|   ",board[1][0],"   |   ",board[1][1],"   |   ",board[1][2],"   |", sep="")
  # print("|       "*3+"|")
  # print("+-------"*3+"+")
  # print("|       "*3+"|")    
  # print("|   ",board[2][0],"   |   ",board[2][1],"   |   ",board[2][2],"   |", sep="")
  # print("|       "*3+"|")
  # print("+-------"*3+"+")
  
  #more compact:
  print("+-------" * 3,"+", sep="")
  for row in range(3):
    print("|       " * 3,"|", sep="")
    for col in range(3):
      print("|   ",board[row][col],"   ", sep = "", end="")
    print("|")
    print("|       " * 3,"|",sep="")
    print("+-------" * 3,"+",sep="")



def enter_move(board):
  # The function accepts the board's current status, asks the user about their move,
  # checks the input, and updates the board according to the user's decision.
  move = False
  while not move:
    try:    
      you = int(input("Enter your move: "))
      move = you >= 1 and you <= 9
      if not move:
        print("Impossible choice - repeat your input!")
        continue      
      for r in range(3):
        if you in board[r]:
          c = board[r].index(you)
          board[r][c] = "O"
          break
      else:   
        print("This field is already taken. Try another!")
        return enter_move(board)        
    except ValueError:
      print("You should enter an integer")
      return enter_move(board)


def make_list_of_free_fields(board):
  # The function browses the board and builds a list of all the free squares; 
  # the list consists of tuples, while each tuple is a pair of row and column numbers.
  free = []
  for r in range(3):
    for el in board[r]:
      if isinstance(el, int):
        free.append((r, board[r].index(el)))
  return free      


def victory_for(board, sign):
  # The function analyzes the board's status in order to check if 
  # the player using 'O's or 'X's has won the game
  
  if sign == "O":
    text = "You won!"
  else:
    text = "Computer won!"
  
  # #checking in rows:
  # for r in range(3): 
  #   count = 0
  #   for el in board[r]:
  #     if el == sign:
  #       count += 1    
  #     if count == 3:
  #       print(text)
  #       break
      
  # #checking in columns:     
  # for c in range(3): 
  #   count = 0
  #   for r in range(3):
  #     if board[r][c] == sign:
  #       count += 1
  #   if count == 3:
  #     print(text)
  #     break

  # #checking in diagonal from top-left to bottom-right    
  # count = 0
  # for i in range(3):    
  #   if board[i][i] == sign:
  #     count += 1
  #   if count == 3:
  #     print(text)    
  #     break
    
  # #checking in diagonal from top-right to bottom-left
  # count = 0  
  # for i in range(3):     
  #   if board[i][2 - i] == sign:
  #     count += 1
  #   if count == 3:
  #     print(text)    
  #     break  


  #compact version:
  
  for i in range(3):
    if all(el == sign for el in board[i])\
      or all(board[j][i] == sign for j in range(3))\
      or all(board[j][j] == sign for j in range(3))\
      or all(board[j][2-j] == sign for j in range(3)):
      print(text)
      return True



def draw_move(board):
  # The function draws the computer's move and updates the board.
  free = make_list_of_free_fields(board)
  cnt = len(free) 
  if cnt > 0:
    comp = randrange(cnt)
    row, col = free[comp]
    board[row][col] = "X"



#game's logic:

board[1][1] = "X"
your_turn = True
free = make_list_of_free_fields(board)
while len(free):  
  display_board(board)
  if your_turn:
    enter_move(board)
    sign = "O"
    if victory_for(board, sign):
      display_board(board)
      break   
  else:
    draw_move(board)
    sign = "X"
    if victory_for(board, sign):
      display_board(board)
      break    
  your_turn = not your_turn
  free = make_list_of_free_fields(board)
else:
  print("Tie!")
  display_board(board)
