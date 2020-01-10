from collections import defaultdict 

class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        self.dict = defaultdict(list) 
    def addEdge(self,u,v,w): 
        self.graph.append([w,u,v]) 
        self.dict[w].append([u,v])
        
    def Dijkstra(self, s): 
        test = [False] * self.V 
        dist = [float('inf')] * self.V
        
        dist[s] = 0
        
        while test != [True] * self.V:
            for i in range(self.V):
                if self.graph[s][i] != 0 and dist[s] + self.graph[s][i] < dist[i]:
                    dist[i] = dist[s] + self.graph[s][i]
                           
            m = float('inf')
            for k in range(self.V):
                if test[k] == False and dist[k] < m :
                    m = dist[k]
                    s = k         
            test[s] = True
            
            diction = {} 
            if test == [True] * self.V:
                for i in range(self.V):
                    diction[str(i)] = dist [i]
                return diction
            
    def Kruskal(self):
        result = {}
        val = sorted(self.dict)
        check = [column for column in range(self.V)]  
        
        for i in val:
            for u,v in self.dict[i]:
                if check[u] == check[v]:
                    pass
                else:
                    check = [check[u]if x==check[v] else x for x in check]
                    result[str(u)+'-'+str(v)] = i
        return result



#https://gist.github.com/econchick/4666413

#https://dev.to/mxl/dijkstras-algorithm-in-python-algorithms-for-beginners-dkc