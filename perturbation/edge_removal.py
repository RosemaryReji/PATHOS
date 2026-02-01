def remove_edge(graph, u, v):
    """
    Returns a COPY of the graph with one edge removed
    """
    g_copy = graph.copy()

    if g_copy.has_edge(u, v):
        g_copy.remove_edge(u, v)

    return g_copy
