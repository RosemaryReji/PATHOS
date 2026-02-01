from itertools import combinations

def path_similarity(p1, p2):
    """
    Jaccard similarity between two paths
    """
    set1, set2 = set(p1), set(p2)
    return len(set1 & set2) / len(set1 | set2)


def ambiguity_score(paths):
    """
    Higher score = more ambiguity
    """
    if len(paths) < 2:
        return 0.0

    similarities = [
        path_similarity(p1, p2)
        for p1, p2 in combinations(paths, 2)
    ]

    avg_similarity = sum(similarities) / len(similarities)
    return round(1 - avg_similarity, 3)
