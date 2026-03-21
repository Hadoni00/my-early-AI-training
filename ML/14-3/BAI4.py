import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
df = pd.read_csv("titanic.csv")
df["Sex"] = df["Sex"].map({"male":0, "female":1})
df["Age"] = df["Age"].fillna(df["Age"].mean())
X = df[["Age","Sex","Pclass","SibSp","Parch"]]
y = df["Fare"]
X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.2,random_state=42
)
model = LinearRegression()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
# evaluate
print("MAE, sai so trung binh:", mean_absolute_error(y_test,y_pred))
print("R2(1:hoan hao, 0:trung binh, < 0:te hon doan bua)  :", r2_score(y_test,y_pred))