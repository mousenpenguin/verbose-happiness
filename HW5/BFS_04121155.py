from collections import defaultdict 

class Graph:
     
    def __init__(self): 
         self.graph = defaultdict(list) 
 
    def addEdge(self,u,v): 
        self.graph[u].append(v)
    

    def BFS(self, s):
        final = []
        queue = [s]
        visited = defaultdict(list)   
        visited[s] = True

        while queue:
            volume = queue.pop(0)
            final.append(volume)
            for t in self.graph[volume]:
                if visited[t] is not True:   
                    visited[t] = True
                    queue.append(t)

        return final
    
    def DFS(self, s):
        final = []
        stack = [s]
        visited = defaultdict(list)    
        visited[s] = True
        while stack:      
            volume = stack.pop()
            final.append(volume)
            for i in self.graph[volume]:
                if visited[i] is not True:   
                    visited[i] = True
                    stack.append(i)
        return final