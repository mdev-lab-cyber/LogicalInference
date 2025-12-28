tik = [
  ["O", "_", "O"],
  ["O", "_", "X"],
  ["X", "X", "_"]
]
from copy import deepcopy

def Terminal_function(stat):
  
    for i in range(3):
        if stat[i][0] == stat[i][1] == stat[i][2] != "_":
            if stat[i][0] == "X":
                return 1
            else:
                return -1
    for i in range(3):
        if stat[0][i] == stat[1][i] == stat[2][i] != "_":
            if stat[0][i] == "X":
                return 1
            else:
                return -1

    if stat[0][0] == stat[1][1] == stat[2][2] != "_":
        if stat[0][0] == "X":
            return 1
        else:
            return -1

  
    if stat[0][2] == stat[1][1] == stat[2][0] != "_":
        if stat[0][2] == "X":
            return 1
        else:
            return -1
    empet = 0
    for i in range(3):
      for j in range(3):
        if stat[i][j] == "_":
          empet += 1
    if empet == 0:
      return 0 # drow
    return None

def pleyr_torn(stat):
    cont_X = 0
    cont_O = 0
    for i in range(3):
      for j in range(3):
        if stat[i][j] == "X":
                cont_X +=1
        if stat[i][j] == "O":
          cont_O += 1
    if cont_X == cont_O:
      return 1 #x
    else:
      return 0 #o
  

def Generate_possible_moves(stat,mark):
    creant_moves = []
    for i in range(3):
      for j in range(3):
        if stat[i][j] == "_":
          new_board = deepcopy(stat)
          new_board[i][j] = mark
          creant_moves.append(new_board)
    return creant_moves
  
def min_pleyr(stat):
  
    result = Terminal_function(stat)
    if result is not None:
      return result
    moves = Generate_possible_moves(stat,"O")
    m = 2
    for board in moves:
       _board = max_pleyr(board)
       if m >  _board:
        m =  _board
    return m
  
  
def max_pleyr(stat):
  result = Terminal_function(stat)
  if result is not None:
    return result
 
  moves = Generate_possible_moves(stat,"X")
  x = -2
  for board in moves:
    
     _board = min_pleyr(board)
     if x < _board :
      x = _board 
  return x
      
def main_function(stat):
  scor = []
  if pleyr_torn(stat) == 1:
    mark = "X"  
  if pleyr_torn(stat) == 0:
    mark = "O"
  for i in range(3):
    for j in range(3):
      if stat[i][j] == "_":
        now_board = deepcopy(stat)
        now_board[i][j] = mark
        best_move = (i,j)
        result = Terminal_function(now_board)
        if result == 1 and mark == "X":
                 return best_move
        if mark == "X":
                value = min_pleyr(now_board)
        else:
                value = max_pleyr(now_board)
        
        scor.append((best_move, value))
  best_scor = -2
  for (move, scort) in scor:
    if scort > best_scor:
      best_scor = scort
      best_move = move
  return best_move
print(main_function(tik))
  
  
    
    
      
  
        
        
     
    
    
  
  
          
          
          
          
          

      
    
    
  


        
        


        
        