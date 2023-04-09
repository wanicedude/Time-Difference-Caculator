hour = int(input("Starting time (hours): "))
minutes = int(input("Starting time (minutes): "))
duration = int(input("Event duration (minutes): "))

a = minutes + duration
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
