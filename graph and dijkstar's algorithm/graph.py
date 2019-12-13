import abc
import numpy as np
#----------------------------------------- implement graph with matrix ------------------------------------
#########################################
# base class respresentation of a graph
# with all the interface methdos 
########################################
class Graph(abc.ABC):
    
    def __init__(self,numVertices,directed=False):
        self.numVertices = numVertices
        self.directed = directed
    
    @abc.abstractmethod
    def add_edge(self,v1,v2,weight):
        pass
    
    @abc.abstractmethod
    def get_adjacent_vertices(self,v):
        pass
    
    @abc.abstractmethod
    def get_indegree(self,v):
        pass
    
    @abc.abstractmethod
    def get_edge_weight(self,v1,v2):
        pass
    
    @abc.abstractmethod
    def display(self):
        pass

#####################################################

# implementation graph with adjacency matrix the cell
# has value if there is edge 
# 0 mean that there is no edge between two vertices
#####################################################
class AdjacencyMatrixGraph(Graph):
    
    def __init__(self,numVertices,directed=False):
        super(AdjacencyMatrixGraph,self).__init__(numVertices,directed)
        self.matrix = np.zeros((numVertices,numVertices))
    
    def add_edge(self,v1,v2,weight=1):
        if v1 >= self.numVertices or v2 >= self.numVertices or v1 <0 or v2 <0:
            raise ValueError(f"Vertices {v1} and {v2} out of bounds")
        
        if weight < 1: 
            raise ValueError("An edge  cannot have weight <1 ")
        
        self.matrix[v1][v2] = weight
        if self.directed == False:
            self.matrix[v2][v1] = weight
    
    def get_adjacent_vertices(self,v):
        if 0 <= v < self.numVertices: 
            adjacent_vertices =[]
            for i in range(self.numVertices):
                if self.matrix[v][i] > 0:
                    adjacent_vertices.append(i)
            return adjacent_vertices
        raise ValueError(f"can not access vertix {v}")
    
    def get_indegree(self,v):
        if v <0 or v >=self.numVertices:
            raise ValueError(f"can not access vertix {v}")
        indegree = 0
        for i in range(self.numVertices):
            if self.matrix[i][v] >0:
                indegree +=1
        return indegree
    
    def get_edge_weight(self,v1,v2):
        return self.matrix[v1][v2]
    
    def display(self):
        for i in range(self.numVertices):
            for v in self.get_adjacent_vertices(i):
                print(f"{i} ----> {v}")

                
