import numpy as np 
import pandas as pd
df = pd.read_csv("titanic.csv")
print("***5 dong dau tien:\n",df.head(5))
print("***kich thuoc dataset: ",df.shape)
print("***ten cac cot:",df.columns)
print("***kieu du lieu tung cot:\n",df.dtypes)
print("***so luong gia tri khong null:",df.count())