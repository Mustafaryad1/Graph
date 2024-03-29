from graph import AdjacencyMatrixGraph
from priority_dict import priority_dict

# Dijkstra's algorithm
def build_distance_table(graph,source):
    distance_table = {}
    
    for i in range(graph.numVertices):
        distance_table[i] = (None,None)
    
    distance_table[source] = (0,source)
    # Holding mapping of vertex id to distance from source
    # Access the highest priority (lowest distance) item 
    # first 
    priority_queue = priority_dict()
    priority_queue[source] = 0
    while len(priority_queue.keys()) >0:
        current_vertex = priority_queue.pop_smallest() # vertex with smallest distance value
        # the distance of current node
        current_distance = distance_table[current_vertex][0]
        for neighbor in graph.get_adjacent_vertices(current_vertex):
            distance = current_distance + graph.get_edge_weight(current_vertex,neighbor)
            neighbor_distance = distance_table[neighbor][0]
            if neighbor_distance is None or neighbor_distance > distance:
                distance_table[neighbor] = (distance,current_vertex)
                priority_queue[neighbor] = distance
    
    return distance_table
            
def shortest_path(graph,source,distination):
    distance_table = build_distance_table(graph,source)
    path = [distination]
    previous_vertex = distance_table[distination][1]
    
    while previous_vertex is not None and previous_vertex is not source:
        path =[previous_vertex] + path
        previous_vertex = distance_table[previous_vertex][1]
        
    if previous_vertex is None:
        print(f"there is no path from {source} to {distination}")
    else:
        path = [source] + path
        print("shortest path is :",path)

        
g = AdjacencyMatrixGraph(8,directed=False)
g.add_edge(0,1,1)
g.add_edge(1,2,2)
g.add_edge(1,3,6)
g.add_edge(2,3,2)
g.add_edge(1,4,3)
g.add_edge(3,5,1)
g.add_edge(5,4,5)
g.add_edge(3,6,1)
g.add_edge(6,7,1)
g.add_edge(0,7,8)

shortest_path(g,0,6) 
shortest_path(g,4,7)
shortest_path(g,7,0)

        