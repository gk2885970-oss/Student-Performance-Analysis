def create_features(df):
    # Average Score
    df["average_score"] = (df["math score"] + df["reading score"] + df["writing score"]) / 3

    # Pass / Fail
    df["result"] = df["average_score"].apply(lambda x: "Pass" if x >= 40 else "Fail")

    # Performance Category
    def performance_category(score):
        if score >= 80:
            return "Excellent"
        elif score >= 60:
            return "Good"
        elif score >= 40:
            return "Average"
        else:
            return "Poor"

    df["performance_category"] = df["average_score"].apply(performance_category)

    print("\n===== Feature Engineering =====")
    print(df[["average_score", "result", "performance_category"]].head(10))

    return df