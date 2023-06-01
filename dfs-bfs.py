# Implement depth first search algorithm and Breadth First Search algorithm, Use an undirected 
# graph and develop a recursive algorithm for searching all the vertices of a graph or tree data 
# structure. 

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# # Take input for the graph
# graph = {}

# num_nodes = int(input("Enter the number of nodes in the graph: "))

# for _ in range(num_nodes):
#     node = input("Enter the node: ")
#     graph[node] = []

# num_edges = int(input("Enter the number of edges in the graph: "))

# for _ in range(num_edges):
#     edge = input("Enter the edge (format: 'node1 node2'): ")
#     node1, node2 = edge.split()
#     graph[node1].append(node2)
#     graph[node2].append(node1)
# take input graph, start node
# initialize visited set

# take start add to set 
# print start

# take start check neighbours in visited if not visited then perform dfs (recurs.)

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    print(start)  # or do whatever processing you want with the node
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
            

print("\nDFS traversal:")
dfs(graph, 'A')


#bfs

from collections import deque

def bfs(graph, start):
    visited = set()       # Set to keep track of visited nodes
    queue = deque([start]) # Queue for BFS traversal

    while queue:
        node = queue.popleft()
        print(node)       # Process the node (e.g., print or store the value)

        if node not in visited:
            visited.add(node)

            # Add adjacent nodes to the queue
            queue.extend(graph[node])
            
print("\nDFS traversal:")
bfs(graph, 'A')
