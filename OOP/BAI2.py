name = input()

# cắt
name = name.strip()

# tách
words = name.split()
words = [w.capitalize() for w in words]

print(" ".join(words))
