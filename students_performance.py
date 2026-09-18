import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df=pd.read_csv(".jetro/StudentsPerformance.csv")

# Basic Data Inspection 
print(df.head())
print(df.shape)
print(df.columns)
df.info()

# Data Quality Checks
duplicate_count = df.duplicated().sum()
print("Number of duplicate rows:", duplicate_count)

print("\nMissing values:")
print(df.isnull().sum())


print("\nScore Range:")
print("Math:", df["math score"].min(),"_",df["math score"].max())
print("Reading", df["reading score"].min(),"_",df["reading score"].max())
print("Writing:", df["writing score"].min(),"_",df["writing score"].max())

# Feature Engineering
df["average_score"]= (df["math score"]+df["reading score"]+df["writing score"])/3

df["result"]=df["average_score"].apply(lambda x:"Pass" if x >= 40 else "Fail")
print(df.head())

def performance_category(score):
    if score >= 80:
        return "Excellent"
    elif score >= 60:
        return "Good"
    elif score >= 40:
        return "Average"
    else:
        return "Poor"
df["performance_category"]=df["average_score"].apply(performance_category)

print("\nFeature Engineering:")
print(df[["average_score","result","performance_category"]].head(10))



# OOP Implemenataion

class Student:

    def __init__(self, math, reading, writing):
        self.math = math
        self.reading = reading
        self.writing = writing

    def average_score(self):
        return (self.math + self.reading + self.writing) / 3

    def pass_or_fail(self):
        if self.average_score() >= 40:
            return "Pass"
        else:
            return "Fail"


# Example student
student1 = Student(70, 80, 75)


# Exploratory Data Analysis
print("Average Score:", student1.average_score())
print("Result:", student1.pass_or_fail())

print("\nOverall Performance:")
print("Average Math Score:",df["math score"].mean())
print("Average Reading Score:",df["reading score"].mean())
print("Average Writing Score:",df["writing score"].mean())
print("Overall Average Score:",df["average_score"].mean())

print("\nPerformance Category Count:")
print(df["performance_category"].value_counts())

print("\nGender-wise Performance:")
gender_performance= df.groupby("gender")[["math score","reading score","writing score","average_score"]].mean()
print(gender_performance)


print("\nTest Preparation-wise Performance:")
prep_performance= df.groupby("test preparation course")[["math score","reading score","writing score","average_score"]].mean()
print(prep_performance)


print("\nLunch-wise Performance:")
lunch_performance=df.groupby("lunch")[["math score","reading score","writing score","average_score"]].mean()
print(lunch_performance)


print("\nParental Education-wise Performance:")
parent_education=df.groupby("parental level of education")[["math score","reading score","writing score","average_score"]].mean()
print(parent_education)


print("\nRace/Ethnicity-wise Performance:")
race_performance=df.groupby("race/ethnicity")[["math score","reading score","writing score","average_score"]].mean()
print(race_performance)


print("\nSubject-wise Performance:")
subject_average=df[["math score","reading score","writing score"]].mean()
print(subject_average)


print("\nCorrelation between Subjects:")
correlation=df[["math score","reading score","writing score","average_score"]].corr()
print(correlation)



#Test Preparation Impact
prep_avg=df.groupby("test preparation course")[["math score","reading score","writing score"]].mean()
prep_avg.plot(kind='bar',figsize=(8,5))
plt.xlabel("Test Preparation Course")
plt.ylabel("Average Score")
plt.title("Student Performance by Test Preparation Course")
plt.legend(title="Subjects")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("test_preparation.png")
plt.show()


# Gender-wise Performance
gender_performance[["math score","reading score","writing score"]].plot(kind='bar',figsize=(8,5))
plt.title("Gender-wise Student Performance")
plt.xlabel("Gender")
plt.ylabel("Average Score")
plt.xticks(rotation=0)
plt.legend(title="Subjects")
plt.tight_layout()
plt.savefig("gender_performance.png")
plt.show()


#Lunch-wise Performance
lunch_performance[["math score","reading score","writing score"]].plot(kind='bar',figsize=(8,5))
plt.title("Lunch-wise Student Performance")
plt.xlabel("Lunch type")
plt.ylabel("Average score")
plt.xticks(rotation=0)
plt.legend(title="Subjects")
plt.tight_layout()
plt.savefig("lunch_performance.png")
plt.show()



# Parental Education-wise Performance
parent_education[["math score","reading score","writing score"]].plot(kind='bar',figsize=(10,6))
plt.title("Parental Education-wise Student Performance")
plt.xlabel("Parental level of Education")
plt.ylabel("Average score")
plt.xticks(rotation=0)
plt.legend(title="Subjects")
plt.tight_layout()
plt.savefig("parent_education.png")
plt.show()


#Race/Ethnicity-wise Performs
race_performance[
    ["math score","reading score","writing score"]
    ].plot(kind='bar',figsize=(10,5)
           )
plt.title("Race/Ethnicity-wise Student Performance")
plt.xlabel("Race/Ethnicity")
plt.ylabel("Average score")
plt.xticks(rotation=0)
plt.legend(title="Subjects")
plt.tight_layout()
plt.savefig("race_performance.png")
plt.show()


#Subject-wise Performance
plt.figure(figsize=(8,5))
subject_average.plot(kind='bar')
plt.title("Subject-wise Student Performance")
plt.xlabel("Subject")
plt.ylabel("Average score")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("subject_average.png")
plt.show()


#Correlation between subjects
plt.figure(figsize=(8,6))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Correlation Between Subjects")
plt.savefig("correlation_heatmap.png")
plt.show()


# Performance Category Distribution

category_count = df["performance_category"].value_counts()

plt.figure(figsize=(8, 5))

category_count.plot(kind="bar")

plt.title("Student Performance Category Distribution")
plt.xlabel("Performance Category")
plt.ylabel("Number of Students")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("performance_category.png")
plt.show()


# Race/Ethnicity vs Average Score - Boxplot

plt.figure(figsize=(8, 5))

sns.boxplot(
    x="race/ethnicity",
    y="average_score",
    data=df
)
plt.title("Average Score Distribution by Race/Ethnicity")
plt.xlabel("Race/Ethnicity")
plt.ylabel("Average Score")
plt.savefig("race_boxplot.png")
plt.show()




# Math Score vs Reading Score - Scatter Plot

plt.figure(figsize=(8, 5))

plt.scatter(
    df["math score"],
    df["reading score"],
    alpha=0.6
)
plt.title("Math Score vs Reading Score")
plt.xlabel("Math Score")
plt.ylabel("Reading Score")
plt.savefig("math_reading_scatter.png")
plt.show()



# Math Score Distribution - Histogram

plt.figure(figsize=(8, 5))

plt.hist(
    df["math score"],
    bins=10,
    edgecolor="black"
)
plt.title("Distribution of Math Scores")
plt.xlabel("Math Score")
plt.ylabel("Number of Students")
plt.savefig("math_histogram.png")
plt.show()





# Final Findings
print("\n=========FINAL FINDINGS==========")
print("1.Reading has the highest average score.")
print("2.Math has the lowest average score.")
print("3.Students who completed test preparation performed better.")
print("4.Students with standard lunch had higher average scores.")
print("5.Group E has the highest average performance.")
print("6.Reading and writing scores have a very strong positive correlation.")
print("7.Most students fall under the Good performance category.")



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

print("\nStudents who completed the test preparation course")
print("achieved higher scores than students who did not.")

print("\nReading has the highest overall average score,")
print("while Math has the lowest average score.")

print("\nOverall, the analysis helps identify the major factors")
print("associated with student academic performance.")

