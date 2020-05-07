from collections import defaultdict 

class graph:
    def __init__(self,vertices):
        self.graph=defaultdict(list)
        self.V=vertices

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def topologicalsortutil(self,v,vertices,stack):
        vertices[v]=True
        for i in self.graph[v]:
            if vertices[i]==False:
                self.topologicalsortutil(i,vertices,stack)
        stack.insert(0,v)
                
    def topologicalsort(self):
        vertices=[False]*self.V
        stack=[]
        for i in range(self.V):
            if vertices[i]==False:
                self.topologicalsortutil(i,vertices,stack)
        print(stack)
                
g= graph(6) 
g.addEdge(5, 2); 
g.addEdge(5, 0); 
g.addEdge(4, 0); 
g.addEdge(4, 1); 
g.addEdge(2, 3); 
g.addEdge(3, 1); 
  
print("Following is a Topological Sort of the given graph")
g.topologicalsort()