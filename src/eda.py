def perform_eda(df):
    print("\n===== Overall Performance =====")
    print("Average Math Score:", round(df["math score"].mean(), 2))
    print("Average Reading Score:", round(df["reading score"].mean(), 2))
    print("Average Writing Score:", round(df["writing score"].mean(), 2))
    print("Overall Average Score:", round(df["average_score"].mean(), 2))

    print("\nPerformance Category Count:")
    print(df["performance_category"].value_counts())

    print("\nGender-wise Performance:")
    print(df.groupby("gender")[["math score", "reading score", "writing score", "average_score"]].mean())

    print("\nTest Preparation-wise Performance:")
    print(df.groupby("test preparation course")[["math score", "reading score", "writing score", "average_score"]].mean())

    print("\nLunch-wise Performance:")
    print(df.groupby("lunch")[["math score", "reading score", "writing score", "average_score"]].mean())

    print("\nParental Education-wise Performance:")
    print(df.groupby("parental level of education")[["math score", "reading score", "writing score", "average_score"]].mean())

    print("\nRace/Ethnicity-wise Performance:")
    print(df.groupby("race/ethnicity")[["math score", "reading score", "writing score", "average_score"]].mean())

    print("\nSubject-wise Performance:")
    print(df[["math score", "reading score", "writing score"]].mean())

    print("\nCorrelation between Subjects:")
    print(df[["math score", "reading score", "writing score", "average_score"]].corr())