import heapq
maze = [
    ['S', '.', '.'],
    ['#', '.', '.'],
    ['.', '.', 'G']
]
def heuristic(start,goal):
    row = start[0]
    colm = start[1]
    row_goal = goal[0]
    colm_goal = goal[1]
    result = abs(row - row_goal) + abs(colm - colm_goal)
    return result
def A_search(start,goal,maze):
    vest = set()
    patch = {}
    frent = []
    patch[start] = None
    total_cost = {} 
    total_cost[start] = 0
    heapq.heappush(frent, (0,start))
    
    while frent:
        
        crent = heapq.heappop(frent)
        crent_1 = crent[1]
        if crent_1 == goal:
            return patch
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
                patch[neighbor] = crent_1
                total_cost[neighbor] = total_cost[crent_1] + 1
                f = heuristic(neighbor, goal) + total_cost[neighbor]
                stat = (f, neighbor)
                heapq.heappush(frent, stat)
               
                
                
print(A_search((0,0),(2,2),maze))
    
    
