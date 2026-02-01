import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter

def draw_heatmap(graph, paths):
    counter = Counter()

    for path in paths:
        for node in path:
            counter[node] += 1

    values = [counter.get(node, 0) for node in graph.nodes()]

    pos = nx.spring_layout(graph)
    nx.draw(
        graph,
        pos,
        with_labels=True,
        node_color=values,
        cmap=plt.cm.inferno,
        node_size=800
    )

    plt.title("Path Usage Heatmap (Decision Ambiguity)")
    plt.show()
