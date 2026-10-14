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

```
Student-Performance-Analysis/
├── data/
│   └── StudentsPerformance.csv
├── visualizations/            (all plots are saved here)
├── results/
│   └── cutoff_analysis_output.txt
├── src/
│   ├── data_loader.py
│   ├── feature_engineering.py
│   ├── student.py
│   ├── eda.py
│   ├── cutoff_analysis.py
│   └── visualization.py
├── main.py
├── requirements.txt
└── README.md
```

## How to Run

```
pip install -r requirements.txt
python main.py                      # full analysis, including the cut-off analysis
python -m src.cutoff_analysis       # only the cut-off and lunch-type analysis
```

## Cut-off and Lunch-Type Analysis

The Pass/Fail result uses a cut-off: a student passes if the average score is 40 or more. The cut-off of 40 is a human choice, not a mathematical rule. `src/cutoff_analysis.py` checks two things:

1. How many students change label when the cut-off moves.
2. How the students below the cut-off are spread across lunch types (standard vs free/reduced).

The full output is saved in `results/cutoff_analysis_output.txt`. Main results (1000 students):

| Check | Result |
|---|---|
| Average score, standard lunch (645 students) | 70.84 |
| Average score, free/reduced lunch (355 students) | 62.20 |
| Students below the cut-off of 40 (Fail) | 30 of 1000 |
| Fail students with free/reduced lunch | 24 of 30 (6.8% of free/reduced students, 0.9% of standard-lunch students) |
| Students labelled Fail at cut-off 35 / 40 / 45 / 50 | 18 / 30 / 54 / 103 |
| Students within 2 points of 40 (38 to under 42) | 17 (10 labelled Fail, 7 labelled Pass) |

The lunch-wise averages are also printed by the EDA step in `main.py`, and the 30 Fail students are the "Poor" category in the performance-category count.

### Limitations

- The dataset is a single snapshot. It has no later outcomes and no time dimension, so it cannot show whether a low score was temporary.
- There is no prediction model in this project, so false-alarm or false-positive rates cannot be calculated from it.
- Lunch type is only a rough sign of family income.
- These results show associations and patterns, not proof of cause.
