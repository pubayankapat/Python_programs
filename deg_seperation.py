import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes (users)
G.add_nodes_from(['Alice', 'Bob', 'Charlie', 'David', 'Eve'])

# Add edges (relationships)
G.add_edges_from([
    ('Alice', 'Bob'),
    ('Bob', 'Charlie'),
    ('Charlie', 'David'),
    ('David', 'Eve')
])

# Find the shortest path length (degrees of separation)
source = 'Alice'
target = 'David'

try:
    degrees = nx.shortest_path_length(G, source=source, target=target)
    print(f"Degrees of Separation between {source} and {target}: {degrees}")
except nx.NetworkXNoPath:
    print(f"No path exists between {source} and {target}")