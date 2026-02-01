import networkx as nx
import matplotlib.pyplot as plt
import random

def draw_paths(graph, paths):
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color="lightgray")

    colors = ["red", "blue", "green", "purple", "orange"]

    for path, color in zip(paths, colors):
        edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(
            graph, pos,
            edgelist=edges,
            edge_color=color,
            width=2
        )

    plt.show()
