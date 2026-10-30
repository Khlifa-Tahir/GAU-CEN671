import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

Gn = nx.DiGraph()


#Add Weighted nodes to the graph
edges = [
(0, 1,{'weight': 1}),(1, 3,{'weight': 2}),(1, 2,{'weight': 1}),(2, 4,{'weight': 2}),
(6, 2,{'weight': 2}),(3, 4,{'weight': 1}),(3, 5,{'weight': 2}),(3, 7,{'weight': 4}),
(4, 5,{'weight': 1}),(4, 6,{'weight': 2}),(5, 7,{'weight': 2}),(5, 8,{'weight': 3}),
(3, 7,{'weight': 1}),(7, 9,{'weight': 2}),(8, 0,{'weight': 2}),(9, 0,{'weight': 1})]

Gn.add_edges_from(edges)

# # Add nodes and edges
# Gn.add_edge("A", "B", weight=3.5)
# Gn.add_edge("B", "C", weight=2.0)
# Gn.add_edge("A", "C", weight=1.5)

#Draw the graph



# plt.figure(figsize=(6,4))
# pos = nx.spring_layout(Gn)
# nx.draw(Gn, pos, with_labels=True, arrows=True)

# plt.figure(figsize=(6,4))
# pos = nx.shell_layout(Gn)
# nx.draw(Gn, pos, with_labels=True, arrows=True)


plt.figure(figsize=(6,4))
pos = nx.circular_layout(Gn)
nx.draw(Gn, pos, with_labels=True, arrows=True)


edge_labels = nx.get_edge_attributes(Gn, 'weight')
nx.draw_networkx_edge_labels(Gn, pos, edge_labels=edge_labels)
plt.show()


fitness=0.0
if Gn.has_edge(4, 5):
    fitness += Gn[4][5]['weight']
    print("...",fitness)
else:
    fitness += 0
fitness = np.power(abs(fitness + 0.9), 2)

print("----------",fitness)

nodes = list(Gn.nodes)
start = nodes[0]
end = nodes[-1]

samples = list(nx.all_simple_paths(Gn, start, end))

print('Nodes',nodes)
print("samples",samples)
