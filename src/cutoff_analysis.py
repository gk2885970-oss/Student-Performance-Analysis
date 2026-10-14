"""Cut-off sensitivity and lunch-type analysis.

Shows how the Pass/Fail rule (average score >= 40) depends on a human-chosen
cut-off, and how the students below the cut-off are spread across lunch types.

Run from the project root:
    python main.py                      # included as the last analysis step
    python -m src.cutoff_analysis       # run on its own
"""
import contextlib
import io

import pandas as pd

PASS_MARK = 40                      # same rule as feature_engineering.py and student.py
CUTOFFS = (35, 40, 45, 50)          # cut-offs compared in the sensitivity table
BAND = 2                            # "near the cut-off" = within 2 points either side


def analyze_cutoffs(df, pass_mark=PASS_MARK, cutoffs=CUTOFFS, band=BAND):
    """Print the cut-off / lunch-type analysis. Expects the 'average_score' column."""
    n = len(df)
    low_income_label = "free/reduced"
    is_fr = df["lunch"] == low_income_label

    print("\n===== Cut-off and Lunch-Type Analysis =====")

    # 1. Average score by lunch type
    print("\nAverage score by lunch type:")
    by_lunch = df.groupby("lunch")["average_score"].agg(["mean", "count"])
    for lunch, row in by_lunch.iterrows():
        print(f"  {lunch:<13} average = {row['mean']:.2f}   students = {int(row['count'])}")
    gap = by_lunch.loc["standard", "mean"] - by_lunch.loc[low_income_label, "mean"]
    print(f"  Gap (standard - free/reduced) = {gap:.2f} points")

    # 2. Students below the pass mark, by lunch type
    fail = df["average_score"] < pass_mark
    n_fail = int(fail.sum())
    fail_fr = int((fail & is_fr).sum())
    fail_std = n_fail - fail_fr
    n_fr = int(is_fr.sum())
    n_std = n - n_fr
    print(f"\nStudents below the pass mark of {pass_mark} (Fail): {n_fail} of {n}")
    print(f"  free/reduced: {fail_fr} of {n_fr} students ({100 * fail_fr / n_fr:.1f}%)")
    print(f"  standard:     {fail_std} of {n_std} students ({100 * fail_std / n_std:.1f}%)")
    print(f"  Share of all Fail students with free/reduced lunch: "
          f"{fail_fr} of {n_fail} ({100 * fail_fr / n_fail:.0f}%)")
    print(f"  Share of all students with free/reduced lunch:      "
          f"{n_fr} of {n} ({100 * n_fr / n:.1f}%)")

    # 3. Cut-off sensitivity
    print("\nCut-off sensitivity (students labelled Fail = average score below the cut-off):")
    print(f"  {'cut-off':>7} | {'Fail':>5} | {'of which free/reduced':>22}")
    for c in cutoffs:
        below = df["average_score"] < c
        print(f"  {c:>7} | {int(below.sum()):>5} | {int((below & is_fr).sum()):>22}")

    # 4. Students close to the pass mark
    near = (df["average_score"] >= pass_mark - band) & (df["average_score"] < pass_mark + band)
    just_below = near & (df["average_score"] < pass_mark)
    print(f"\nStudents within {band} points of the pass mark "
          f"({pass_mark - band} <= average < {pass_mark + band}): {int(near.sum())}")
    print(f"  just below {pass_mark} (labelled Fail): {int(just_below.sum())}")
    print(f"  {pass_mark} or above (labelled Pass):   {int(near.sum() - just_below.sum())}")


if __name__ == "__main__":
    from src.feature_engineering import create_features

    data = pd.read_csv("data/StudentsPerformance.csv")
    with contextlib.redirect_stdout(io.StringIO()):   # create_features prints a preview table
        data = create_features(data)
    analyze_cutoffs(data)
