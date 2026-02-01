from abc import ABC, abstractmethod

class PathExplorationStrategy(ABC):
    @abstractmethod
    def explore(self, graph, start, end, max_paths):
        pass
