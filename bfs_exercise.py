graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}
def BFS(start,graph,goal):
    frent = [start]
    vest = set()
    prent = {start : None}
    while frent:
        crent = frent[0]
        frent.pop(0)
        if crent == goal:
             break
        vest.add(crent)
        for neighbors in graph[crent]:
             if neighbors in vest:
                 continue
             if neighbors  not in frent:
                 frent.append(neighbors)
                 prent[neighbors] = crent
    if goal not in prent:
        return None
    patch =[]
    node = goal
    while node is not None:
        patch.append(node)
        node = prent[node]
    patch.reverse()
    return patch
print(BFS('A',graph,'o'))


        
    
    
            

                 
        
        
         
        
    
    
    
    
    
        
        
    
    