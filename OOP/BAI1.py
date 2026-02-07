import random
import math

n = int(input())

a = [random.randint(1, 100) for _ in range(n)]

# in danh sách ban đầu
print(*a)

# sắp xếp
a.sort()
print(*a)

mn = min(a)
mx = max(a)
mean = sum(a) / n

var = sum((x - mean) ** 2 for x in a) / n
stddev = math.sqrt(var)

print("Min =", mn)
print("Max =", mx)
print("Mean =", mean)
print("Variance =", var)
print("StdDev =", stddev)
