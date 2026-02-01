import random
from exploration.base_strategy import PathExplorationStrategy

class RandomizedDFS(PathExplorationStrategy):
    def explore(self, graph, start, end, max_paths=20):
        discovered = set()

        def dfs(node, path):
            if len(discovered) >= max_paths:
                return
            if node == end:
                discovered.add(tuple(path))
                return

            neighbors = list(graph.neighbors(node))
            random.shuffle(neighbors)  # KEY NON-DETERMINISM

            for n in neighbors:
                if n not in path:
                    dfs(n, path + [n])

        for _ in range(max_paths * 2):
            dfs(start, [start])

        return [list(p) for p in discovered]
