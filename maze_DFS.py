
#maze =[['S', ' ', ' ', '#'],
  #['#', '#', ' ', '#'],
  #[' ', ' ', ' ', 'G']
#]
def DFS_sol(start,goal,maze):
    prent = {}
    len_row = len(maze)
    len_colm = len(maze[0])
    prent[start] = None
    visited = set()
    stack = []
    stack.append(start)#stack[start]
    
    while stack:
        crent = stack.pop()
        if crent == goal:
            return prent
        if crent not in visited:
            visited.add(crent)#[s]
            row =crent[0]
            col =crent[1]
            up = (row -1,col)#Generate neighbors
            down = (row + 1,col)
            left = (row,col-1)
            right = (row,col +1)
            neighbors = [up, down, left, right]
            for neighbor in neighbors:
                r = neighbor[0]
                c = neighbor[1]
                if (len_row > r >= 0) and (len_colm > c >=0) and maze[r][c] != '#' and (neighbor not in visited) :
                    stack.append(neighbor)
                    prent[neighbor] = crent
                    
                    
                
                
                

            
            
            
            

 
     
      
       
            
            
     
            
        

