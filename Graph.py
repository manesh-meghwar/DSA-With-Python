class Graph:
    def __init__(self, vno):
        self.vertex_count = vno
        self.adj_matrix = [ [0]*vno for e in range(vno)]
        
    # Add edge in the graph
    def add_edge(self, u, v, weight=1):         # u = starting edge, v = ending edge, like (u,v) and have value like (0,1)
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight
        else:
            print("Invalid Vertex")
            
    # Remove edge in the graph
    def remove_edge(self, u, v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v] = 0
            self.adj_matrix[v][u] = 0
        else:
            print("Invalid Vertex")
          
          
    # Check edge in the graph exist or not  
    def has_edge(self, u, v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            return self.adj_matrix[u][v] != 0
        else:
            print("Invalid Vetrex")
            
            
    # Print the Graph matrix (adj_matix)
    def print_adj_matrix(self):
        for row_list in self.adj_matrix:
            print(" ".join(map(str, row_list)))
            
            
g = Graph(5)

# g.add_edge(0,1)
# g.add_edge(1,2)
# g.add_edge(1,3)
# g.add_edge(2,3)
# g.add_edge(3,4)

# g.print_adj_matrix()




g.add_edge(0,1,3)
g.add_edge(1,2,2)
g.add_edge(1,3,1)
g.add_edge(2,3,1)
g.add_edge(3,4,2)

g.print_adj_matrix()