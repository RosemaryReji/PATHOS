import networkx as nx

def load_demo_graph():
    G = nx.Graph()
    edges = [
        ("A", "B"), ("B", "D"),
        ("A", "C"), ("C", "E"),
        ("E", "B"), ("E", "D"),
        ("C", "D")
    ]
    G.add_edges_from(edges)
    return G
