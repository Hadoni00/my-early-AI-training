import pandas as pd
df = pd.read_csv("titanic.csv")
phu_nu = df[df["Sex"] == "female"]
print("so hanh khach nu:",phu_nu)
child = df[df["Age"] < 18]
print("so hanh khach < 18 tuoi:",child)
first_class = df[df["Pclass"] == 1]
print("so hanh khach hang 1:",first_class)
#nam >=40
old = df[(df["Sex"] == "male") & (df["Age"] >= 40)]
print("so hanh khac nam >=40 tuoi:",old)
print("so nam,nu:\n",df["Sex"].value_counts())
print("so hanh khach song:", (df["Survived"] == 1).sum())
print("so hanh khach khong song:", (df["Survived"] == 0).sum())