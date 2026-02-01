from datetime import datetime

def generate_report(before_score, after_score=None, removed_edge=None):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report = f"""
# PATHOS Experiment Report

Time: {timestamp}

## Baseline
Ambiguity Score: {before_score}

"""

    if after_score is not None:
        report += f"""
## Perturbation
Removed Edge: {removed_edge[0]}-{removed_edge[1]}
Ambiguity Score After Perturbation: {after_score}

## Change
Ambiguity Difference: {round(before_score - after_score, 3)}
"""

    with open("reports/latest_report.md", "w") as f:
        f.write(report)
