mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
a = mins + dura
x = a // 60
y = a % 60
hour = (hour + x)
mins = y
if hour < 24:
    print(f"{hour}:{y}")
elif hour > 24 and hour - 24 < 24:
    hour = hour - 24
    print(f"{hour}:{y}")
else:
    hour = x % 24
    print(f"{hour}:{y}")
