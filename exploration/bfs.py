from collections import deque
from exploration.base_strategy import PathExplorationStrategy

class BFS(PathExplorationStrategy):
    def explore(self, graph, start, end, max_paths=1):
        queue = deque([(start, [start])])

        while queue:
            node, path = queue.popleft()
            if node == end:
                return [path]

            for neighbor in graph.neighbors(node):
                if neighbor not in path:
                    queue.append((neighbor, path + [neighbor]))

        return []
