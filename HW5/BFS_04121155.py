from collections import defaultdict 

class Graph:
     
    def __init__(self): 
         self.graph = defaultdict(list) 
 
    def addEdge(self,u,v): 
        self.graph[u].append(v)
    
    
    def BFS(self, s):
        visited = []
        queue = [s]

        while queue:
            s = queue.pop(0)
            for u in graph[s]:
                if i not in visited:
                    visited.append(i)
                    queue.append(i)

        return visited

    def DFS(self, s):
        visited = [s]
        stack = [s]

        while stack:
            s = stack[-1]
            if s not in visited:
                visited.extend(s)
            remove_from_stack = True

            for next in self[s]:
                if next not in visited:
                    stack.extend(next)
                    remove_from_stack = False
                    break
            if remove_from_stack:
                stack.pop()

        return visited



        #https://www.geeksforgeeks.org/difference-between-bfs-and-dfs/

        #https://www.educative.io/edpresso/dfs-vs-bfs

        #http://mishadoff.com/blog/dfs-on-binary-tree-array/

        #ppt
