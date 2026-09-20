import matplotlib.pyplot as plt
import seaborn as sns
import os

def create_visualizations(df):
    os.makedirs("visualizations", exist_ok=True)

    # 1. Test Preparation
    prep_avg = df.groupby("test preparation course")[["math score", "reading score", "writing score"]].mean()
    prep_avg.plot(kind='bar', figsize=(8, 5))
    plt.title("Student Performance by Test Preparation Course")
    plt.xlabel("Test Preparation Course")
    plt.ylabel("Average Score")
    plt.xticks(rotation=0)
    plt.legend(title="Subjects")
    plt.tight_layout()
    plt.savefig("visualizations/test_preparation.png")
    plt.close()

    # 2. Gender-wise
    gender_performance = df.groupby("gender")[["math score", "reading score", "writing score"]].mean()
    gender_performance.plot(kind='bar', figsize=(8, 5))
    plt.title("Gender-wise Student Performance")
    plt.xlabel("Gender")
    plt.ylabel("Average Score")
    plt.xticks(rotation=0)
    plt.legend(title="Subjects")
    plt.tight_layout()
    plt.savefig("visualizations/gender_performance.png")
    plt.close()

    # 3. Lunch-wise
    lunch_performance = df.groupby("lunch")[["math score", "reading score", "writing score"]].mean()
    lunch_performance.plot(kind='bar', figsize=(8, 5))
    plt.title("Lunch-wise Student Performance")
    plt.xlabel("Lunch Type")
    plt.ylabel("Average Score")
    plt.xticks(rotation=0)
    plt.legend(title="Subjects")
    plt.tight_layout()
    plt.savefig("visualizations/lunch_performance.png")
    plt.close()

    # 4. Parental Education
    parent_education = df.groupby("parental level of education")[["math score", "reading score", "writing score"]].mean()
    parent_education.plot(kind='bar', figsize=(10, 6))
    plt.title("Parental Education-wise Student Performance")
    plt.xlabel("Parental Level of Education")
    plt.ylabel("Average Score")
    plt.xticks(rotation=45)
    plt.legend(title="Subjects")
    plt.tight_layout()
    plt.savefig("visualizations/parent_education.png")
    plt.close()

    # 5. Race/Ethnicity
    race_performance = df.groupby("race/ethnicity")[["math score", "reading score", "writing score"]].mean()
    race_performance.plot(kind='bar', figsize=(10, 5))
    plt.title("Race/Ethnicity-wise Student Performance")
    plt.xlabel("Race/Ethnicity")
    plt.ylabel("Average Score")
    plt.xticks(rotation=0)
    plt.legend(title="Subjects")
    plt.tight_layout()
    plt.savefig("visualizations/race_performance.png")
    plt.close()

    # 6. Subject Average
    subject_average = df[["math score", "reading score", "writing score"]].mean()
    plt.figure(figsize=(8, 5))
    subject_average.plot(kind='bar')
    plt.title("Subject-wise Average Score")
    plt.xlabel("Subject")
    plt.ylabel("Average Score")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig("visualizations/subject_average.png")
    plt.close()

    # 7. Correlation Heatmap
    correlation = df[["math score", "reading score", "writing score", "average_score"]].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Between Subjects")
    plt.tight_layout()
    plt.savefig("visualizations/correlation_heatmap.png")
    plt.close()

    # 8. Performance Category
    category_count = df["performance_category"].value_counts()
    plt.figure(figsize=(8, 5))
    category_count.plot(kind="bar")
    plt.title("Student Performance Category Distribution")
    plt.xlabel("Performance Category")
    plt.ylabel("Number of Students")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig("visualizations/performance_category.png")
    plt.close()

    # 9. Race Boxplot
    plt.figure(figsize=(8, 5))
    sns.boxplot(x="race/ethnicity", y="average_score", data=df)
    plt.title("Average Score Distribution by Race/Ethnicity")
    plt.xlabel("Race/Ethnicity")
    plt.ylabel("Average Score")
    plt.tight_layout()
    plt.savefig("visualizations/race_boxplot.png")
    plt.close()

    # 10. Math vs Reading Scatter
    plt.figure(figsize=(8, 5))
    plt.scatter(df["math score"], df["reading score"], alpha=0.6)
    plt.title("Math Score vs Reading Score")
    plt.xlabel("Math Score")
    plt.ylabel("Reading Score")
    plt.tight_layout()
    plt.savefig("visualizations/math_reading_scatter.png")
    plt.close()

    # 11. Math Histogram
    plt.figure(figsize=(8, 5))
    plt.hist(df["math score"], bins=10, edgecolor="black")
    plt.title("Distribution of Math Scores")
    plt.xlabel("Math Score")
    plt.ylabel("Number of Students")
    plt.tight_layout()
    plt.savefig("visualizations/math_histogram.png")
    plt.close()

    print("\nAll visualizations saved in 'visualizations' folder.")