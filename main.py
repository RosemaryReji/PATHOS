from ingestion.graph_loader import load_demo_graph
from exploration.randomized_dfs import RandomizedDFS
from solution_space.path_store import PathStore

def main():
    graph = load_demo_graph()

    explorer = RandomizedDFS()
    store = PathStore()

    paths = explorer.explore(graph, "A", "D", max_paths=15)
    store.add_paths(paths)

    print("Discovered paths:")
    for p in store.all_paths():
        print(p)

    print("\nTotal unique paths:", store.count())

if __name__ == "__main__":
    main()
