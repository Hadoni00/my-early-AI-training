name = input("Nhap vao ten cua ban: ")

# cắt
name = name.strip()

# tách
words = name.split()
words = [w.capitalize() for w in words]

print(" ".join(words))
