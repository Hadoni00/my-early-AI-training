import pandas as pd
df = pd.read_csv("titanic.csv")
print(df.describe())
print("Tuoi trung binh:", df["Age"].mean())
print("Gia ve cao nhat:", df["Fare"].max())
print("Tuoi nho nhat:", df["Age"].min())