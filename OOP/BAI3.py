from datetime import datetime, timedelta

# input: YYYY-mm-dd
s = input().strip()
birth = datetime.strptime(s, "%Y-%m-%d")

now = datetime.now()

# a) số ngày đã sống
days_lived = (now - birth).days
print("So ngay da song:", days_lived)

# b) Unix timestamp ngày sinh
print("Unix timestamp ngay sinh:", int(birth.timestamp()))

# c) mốc 49 và 100 ngày (giả định mất 23/04/2100)
death = datetime(2100, 4, 23)

print("Moc 49 ngay:", int((death + timedelta(days=49)).timestamp()))
print("Moc 100 ngay:", int((death + timedelta(days=100)).timestamp()))
