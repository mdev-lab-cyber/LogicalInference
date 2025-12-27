maze = [
    ['S', '.', '.'],
    ['#', '.', '.'],
    ['.', '.', 'G']
]
import heapq

def UCS(start,maze,goal):
     vest = set()
     prent = {}
     prent[start] = None
     frent = []
  
     heapq.heappush(frent, (0,start))

     while frent:
         crent = heapq.heappop(frent)
         crent_1 = crent[1]
         if crent_1 == goal:
             return prent
         if crent_1 not in vest:
             vest.add(crent_1)#s
         row = crent_1[0]
         colm = crent_1[1]
         up = (row-1,colm)
         down = (row+1,colm)
         left = (row,colm-1)
         right = (row,colm+1)
         len_row = len(maze)
         len_colm = len(maze[0])
         neighbors = [up, down, left, right]
         for neighbor in neighbors:
            r = neighbor[0]
            c = neighbor[1]
            if (len_row > neighbor[0] >= 0) and (len_colm > neighbor[1] >= 0) and maze[r][c] != '#' and neighbor not in vest:
                prent[neighbor] = crent_1
                cost = crent[0] + 1
                cost_stat = (cost,neighbor)
                heapq.heappush(frent, cost_stat)
                
             
             
    
     
     
     
