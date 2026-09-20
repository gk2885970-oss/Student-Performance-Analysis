# Student Performance Analysis

## About the Project

This project analyzes the academic performance of 1000 students using Python.  
The goal is to understand how different factors like gender, test preparation, lunch type, parental education, and race/ethnicity are related to student scores in Math, Reading, and Writing.

## Dataset

- **Source:** Students Performance in Exams dataset
- **Records:** 1000 students
- **Columns:**
  - Gender
  - Race/Ethnicity
  - Parental Level of Education
  - Lunch
  - Test Preparation Course
  - Math Score
  - Reading Score
  - Writing Score

## What I Did

1. Loaded and inspected the dataset
2. Checked for missing values and duplicates
3. Created new features:
   - Average Score
   - Pass/Fail Result
   - Performance Category (Poor, Average, Good, Excellent)
4. Used Object-Oriented Programming (Student class)
5. Performed Exploratory Data Analysis (EDA)
6. Created multiple visualizations
7. Summarized key findings and recommendations

## Project Structure

Student-Performance-Analysis/ │ ├── data/ │   └── StudentsPerformance.csv │ ├── visualizations/ │   └── (all plots are saved here) │ ├── src/ │   ├── data_loader.py │   ├── feature_engineering.py │   ├── student.py │   ├── eda.py │   └── visualization.py │ ├── main.py ├── requirements.txt └── README.md