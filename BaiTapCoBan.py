# # ================== BÀI CƠ BẢN ==================

# # 1.
# print("Welcome to Python")


# # 2.
# number = int(input("Nhap vao so nguyen: "))
# if number % 2 == 0:
#     print("So chan")
# else:
#     print("So le")


# # 3. BMI
# def phan_loai_bmi(bmi):
#     if bmi < 18.5:
#         return "Gay"
#     elif bmi <= 22.9:
#         return "Binh thuong"
#     elif bmi <= 24.9:
#         return "Thua can"
#     else:
#         return "Beo phi"

# weight = float(input("Nhap can nang (kg): "))
# height = float(input("Nhap chieu cao (m): "))
# bmi = weight / (height * height)
# print("BMI:", round(bmi, 2), "-", phan_loai_bmi(bmi))


# # 4. Tổng 1..n
# n = int(input("Nhap n: "))
# s = 0
# for i in range(1, n + 1):
#     s += i
# print("Tong:", s)


# # 5. Đếm số chia hết cho 2,3,5,7
# i = 1
# cnt = 0
# while i <= n:
#     if i % 2 == 0 and i % 3 == 0 and i % 5 == 0 and i % 7 == 0:
#         cnt += 1
#     i += 1
# print("So chia het cho 2,3,5,7:", cnt)


# # 6. Bài trăm gà
# for dung in range(1, 21):
#     for nam in range(1, 34):
#         gia = 100 - dung - nam
#         if gia > 0 and 5*dung + 3*nam + gia/3 == 100:
#             print("Dung:", dung, "Nam:", nam, "Gia:", gia)


# # ================== BÀI 1 – THỐNG KÊ ==================
import random
import math

# N = 10
# a = [random.randint(0, 10) for _ in range(N)]

# with open("data.txt", "w") as f:
#     for x in a:
#         f.write(str(x) + " ")

# with open("data.txt", "r") as f:
#     a = list(map(int, f.read().split()))

# n = len(a)
# mean = sum(a) / n
# var = sum((x - mean) ** 2 for x in a) / n
# std = math.sqrt(var)

# a.sort()

# with open("out_bai1.txt", "w", encoding="utf-8") as f:
#     f.write("Danh sach sau khi sap xep:\n")
#     f.write(" ".join(map(str, a)) + "\n")
#     f.write(f"Trung binh: {mean}\n")
#     f.write(f"Phuong sai: {var}\n")
#     f.write(f"Do lech chuan: {std}\n")


# ================== BÀI 2 – KHOẢNG CÁCH ==================
# points = [(1, 2), (3, 4), (5, 9)]

# with open("points.txt", "w") as f:
#     for x, y in points:
#         f.write(f"{x},{y}\n")

# pts = []
# with open("points.txt", "r") as f:
#     for line in f:
#         x, y = map(float, line.strip().split(","))
#         pts.append((x, y))

# dist = []
# for x, y in pts:
#     d = math.sqrt(x*x + y*y)
#     dist.append(d)

# n = len(dist)
# mean_d = sum(dist) / n
# var_d = sum((d - mean_d) ** 2 for d in dist) / n

# with open("out_bai2.txt", "w", encoding="utf-8") as f:
#     for i, d in enumerate(dist, 1):
#         f.write(f"d{i} = {d}\n")
#     f.write(f"Khoang cach trung binh: {mean_d}\n")
#     f.write(f"Phuong sai khoang cach: {var_d}\n")


# ================== BÀI 3 – SET & XÁC SUẤT ==================
# N = 1000
# rolls = [random.randint(1, 6) for _ in range(N)]

# with open("dice.txt", "w") as f:
#     for x in rolls:
#         f.write(str(x) + "\n")

# with open("dice.txt") as f:
#     data = [int(line.strip()) for line in f]

# cnt = {}
# for x in data:
#     cnt[x] = cnt.get(x, 0) + 1

# faces = set(data)

# with open("out_bai3.txt", "w", encoding="utf-8") as f:
#     f.write(f"Các mặt xuất hiện: {sorted(faces)}\n")
#     for face in range(1, 7):
#         prob = cnt.get(face, 0) / N
#         f.write(f"Mặt {face}: {prob:.3f}\n")

# BAI 4 ============================
# data = {}

# with open("students.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         name, cls, score = line.strip().split(",")
#         score = float(score)

#         if cls not in data:
#             data[cls] = []
#         data[cls].append(score)

# # ====== TÍNH TOÁN ======
# def mean(a):
#     return sum(a) / len(a)

# def variance(a, m):
#     return sum((x - m) ** 2 for x in a) / len(a)

# # ====== OUTPUT ======
# with open("out.txt", "w", encoding="utf-8") as f:
#     for cls in sorted(data.keys()):
#         scores = data[cls]
#         n = len(scores)
#         m = mean(scores)
#         v = variance(scores, m)
#         std = math.sqrt(v)

#         f.write(f"Lớp {cls}\n")
#         f.write(f"Số học sinh: {n}\n")
#         f.write(f"Trung bình: {m:.2f}\n")
#         f.write(f"Phương sai: {v:.2f}\n")
#         f.write(f"Độ lệch chuẩn: {std:.2f}\n\n")