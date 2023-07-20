import networkx
import matplotlib.pyplot as plt


NewGraph = networkx.Graph()
NewGraph.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F', 'G'])


NewGraph.add_edges_from(
    [('A', 'B', {"distance": 20}),
     ('A', 'C', {"distance": 10}),
     ('A', 'D', {"distance": 15}),
     ('A', 'E', {"distance": 11}),
     ('A', 'G', {"distance": 35}),
     ('B', 'C', {"distance": 24}),
     ('B', 'D', {"distance": 12}),
     ('B', 'E', {"distance": 12}),
     ('B', 'F', {"distance": 23}),
     ('B', 'G', {"distance": 45}),
     ('C', 'E', {"distance": 11}),
     ('C', 'F', {"distance": 13}),
     ('C', 'G', {"distance": 35}),
     ('D', 'C', {"distance": 24}),
     ('E', 'D', {"distance": 12}),
     ('F', 'E', {"distance": 12}),
     ('G', 'F', {"distance": 23}),
     ('D', 'G', {"distance": 45})
     ])

pos_nodes = {
    "A": (1, 2),
    "B": (2, 4),
    "C": (3, 6),
    "D": (4, 2),
    "E": (5, 6),
    "F": (6, 2),
    "G": (7, 6)
}
edge_labels = {(u, v): d["distance"] for u, v, d in NewGraph.edges(data=True)}
# This code generates a basic plot for the graph and then
# shows the resulting graph value.
networkx.draw(NewGraph,
              pos_nodes,
              with_labels=True)
networkx.draw_networkx_edge_labels(
    NewGraph, pos_nodes, edge_labels=edge_labels, label_pos=0.5)

plt.show()
