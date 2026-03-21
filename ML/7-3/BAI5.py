import pandas as pd
import re

df = pd.read_csv("titanic.csv")

# 1. Sex -> 0/1
df["Sex"] = df["Sex"].map({"male":0, "female":1})
print("chuyen cot Sex thanh 0/1")

# bo chu, giu so
df["Cabin"] = df["Cabin"].str.extract("(\\d+)")
# chuyen sang so thuc
df["Cabin"] = df["Cabin"].astype(float)
print("Cabin sau khi xu ly:")
print(df["Cabin"].head())