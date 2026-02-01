class PathStore:
    def __init__(self):
        self.paths = []

    def add_paths(self, new_paths):
        for p in new_paths:
            if p not in self.paths:
                self.paths.append(p)

    def all_paths(self):
        return self.paths

    def count(self):
        return len(self.paths)
