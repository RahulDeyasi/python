class AdjNode:
    def __init__(self,data):
        self.vertex = data
        self.next  = None
class Graph:
    def __init__(self,vertices):
        self.V  = vertices
        self.graph = [None] * self.V
    def add_edge(self,src,dest):
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src]=node

        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def DFT(self,root,visited):
        if root not in visited:
            print(root, end =' ')
            visited.add(root)

            for neighbour in self.graph[root]:
                DFT(neighbour,visited)
if __name__ == "__main__":
    V = int(input())
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    visited = set()
    graph.DFT(2,visited)
            
        
        
