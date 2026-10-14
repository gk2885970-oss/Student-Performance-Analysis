from src.data_loader import load_data
from src.feature_engineering import create_features
from src.student import Student
from src.eda import perform_eda
from src.visualization import create_visualizations
from src.cutoff_analysis import analyze_cutoffs

def main():
    print("===== STUDENT PERFORMANCE ANALYSIS =====\n")

    # 1. Load Data
    df = load_data()

    # 2. Feature Engineering
    df = create_features(df)

    # 3. OOP Example
    student1 = Student(70, 80, 75)
    print("\n===== OOP Example =====")
    print("Average Score:", student1.average_score())
    print("Result:", student1.pass_or_fail())

    # 4. EDA
    perform_eda(df)
    analyze_cutoffs(df)
    # 5. Visualizations
    create_visualizations(df)

    # 6. Final Findings
    print("\n========= FINAL FINDINGS ==========")
    print("1. Reading has the highest average score.")
    print("2. Math has the lowest average score.")
    print("3. Students who completed test preparation performed better.")
    print("4. Students with standard lunch had higher average scores.")
    print("5. Group E has the highest average performance.")
    print("6. Reading and Writing scores have a very strong positive correlation.")
    print("7. Most students fall under the Good performance category.")

    print("\n========== RECOMMENDATIONS ==========")
    print("1. Encourage students to complete test preparation courses.")
    print("2. Provide additional support for students weak in Mathematics.")
    print("3. Give extra academic support to students with lower scores.")
    print("4. Encourage regular study and practice.")
    print("5. Use student performance data to identify areas for improvement.")

    print("\n========== CONCLUSION ==========")
    print("The analysis shows associations between student performance")
    print("and factors such as test preparation, lunch type,")
    print("parental education and race/ethnicity.")

if __name__ == "__main__":
    main()
