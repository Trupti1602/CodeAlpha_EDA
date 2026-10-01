from ucimlrepo import fetch_ucirepo
import pandas as pd


student_performance = fetch_ucirepo(id=320)

X = student_performance.data.features
y = student_performance.data.targets


df = pd.concat([X, y], axis=1)

df.to_csv("data/student_performance.csv", index=False)

print("Dataset downloaded successfully!")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")
print("\nFirst 5 rows:")
print(df.head())