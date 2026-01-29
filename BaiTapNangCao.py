import torch
import numpy as np
import torch
a = []
with open("scores_matrix.txt") as f:
	for line in f:
		a.append(list(map(float,line.split(","))))
tensor_a = torch.tensor(a,dtype=torch.float32)
height,width = tensor_a.shape
tensor_average = tensor_a.mean(dim=1)
tensor_var = tensor_a.var(dim=1)
tensor_std= tensor_a.std(dim=1)
print(f"average of students: {tensor_average}")
print(f"variance of students: {tensor_var}")
print(f"stadard deviation of students: {tensor_std}")