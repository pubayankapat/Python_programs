import networkx as nx
import matplotlib.pyplot as plt

# Initialize an empty graph
G = nx.Graph()

# Add initial nodes and edges
G.add_nodes_from([1, 2, 3])
G.add_edges_from([(1, 2), (2, 3)])

# Plot the initial graph
nx.draw(G, with_labels=True)
plt.show()

# Dynamically add a node and edge
G.add_node(4)
G.add_edge(3, 4)

# Plot the updated graph
nx.draw(G, with_labels=True)
plt.show()

# Remove an edge and a node
G.remove_edge(2, 3)
G.remove_node(1)

# Plot the final graph
nx.draw(G, with_labels=True)
plt.show()
