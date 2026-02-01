import argparse

from ingestion.graph_loader import load_demo_graph
from exploration.randomized_dfs import RandomizedDFS
from solution_space.path_store import PathStore
from ambiguity.metrics import ambiguity_score
from visualization.graph_view import draw_paths
from perturbation.edge_removal import remove_edge
from reports.generator import generate_report


def main():
    # ---------------- CLI ARGUMENTS ----------------
    parser = argparse.ArgumentParser(
        description="PATHOS: Ambiguity Explorer"
    )

    parser.add_argument(
        "--paths",
        type=int,
        default=20,
        help="Number of paths to explore"
    )

    parser.add_argument(
        "--remove-edge",
        nargs=2,
        metavar=("U", "V"),
        help="Remove an edge (U V) to test perturbation"
    )

    args = parser.parse_args()

    # ---------------- LOAD GRAPH ----------------
    graph = load_demo_graph()

    explorer = RandomizedDFS()

    # ---------------- BEFORE PERTURBATION ----------------
    store_before = PathStore()
    paths_before = explorer.explore(
        graph, "A", "D", max_paths=args.paths
    )
    store_before.add_paths(paths_before)

    score_before = ambiguity_score(store_before.all_paths())

    print("\n=== BEFORE PERTURBATION ===")
    print("Ambiguity Score:", score_before)

    draw_paths(graph, store_before.all_paths()[:5])

    # Generate baseline report
    generate_report(score_before)

    # ---------------- AFTER PERTURBATION (OPTIONAL) ----------------
    if args.remove_edge:
        u, v = args.remove_edge
        print(f"\nRemoving edge {u}-{v}...\n")

        perturbed_graph = remove_edge(graph, u, v)

        store_after = PathStore()
        paths_after = explorer.explore(
            perturbed_graph, "A", "D", max_paths=args.paths
        )
        store_after.add_paths(paths_after)

        score_after = ambiguity_score(store_after.all_paths())

        print("=== AFTER PERTURBATION ===")
        print("Ambiguity Score:", score_after)

        draw_paths(perturbed_graph, store_after.all_paths()[:5])

        # Generate comparison report
        generate_report(score_before, score_after, (u, v))


if __name__ == "__main__":
    main()
