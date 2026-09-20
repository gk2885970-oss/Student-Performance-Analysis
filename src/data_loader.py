import pandas as pd

def load_data(file_path="data/StudentsPerformance.csv"):
    df = pd.read_csv(file_path)

    print("===== Basic Data Inspection =====")
    print(df.head())
    print("\nShape:", df.shape)
    print("\nColumns:", df.columns.tolist())
    print("\nInfo:")
    df.info()

    print("\n===== Data Quality Checks =====")
    print("Number of duplicate rows:", df.duplicated().sum())
    print("\nMissing values:")
    print(df.isnull().sum())

    print("\nScore Range:")
    print("Math:", df["math score"].min(), "-", df["math score"].max())
    print("Reading:", df["reading score"].min(), "-", df["reading score"].max())
    print("Writing:", df["writing score"].min(), "-", df["writing score"].max())

    return df