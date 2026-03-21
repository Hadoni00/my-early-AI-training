import pandas as pd
df = pd.read_csv("titanic.csv")
df["Age_zscore"] = (df["Age"] - df["Age"].mean()) / df["Age"].std()
print("Age sau khi Z-score:")
print(df["Age_zscore"].head())
df["Fare_minmax"] = (df["Fare"] - df["Fare"].min()) / (df["Fare"].max() - df["Fare"].min())
print("Fare sau khi Min-Max:")
print(df["Fare_minmax"].head())