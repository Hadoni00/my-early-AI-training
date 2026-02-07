from datetime import datetime, timedelta

# input: YYYY-mm-dd
s = input().strip()
birth = datetime.strptime(s, "%Y-%m-%d")
now = datetime.now()

# a) số ngày 
print("So ngay da song:", (now - birth).days)

# b) Unix timestamp ngày sinh
print("Unix timestamp ngay sinh:", int(birth.timestamp()))

# c) mốc 49 và 100 
death = datetime(2100, 4, 23)

day_49 = death + timedelta(days=49)
day_100 = death + timedelta(days=100)

print("Moc 49 ngay:", day_49.strftime("%d/%m/%Y"))
print("Moc 100 ngay:", day_100.strftime("%d/%m/%Y"))
