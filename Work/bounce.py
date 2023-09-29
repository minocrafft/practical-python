# bounce.py
# Exercise 1.5

bounce = 60.0

for i in range(1, 11):
    print(i, bounce)
    bounce = round(bounce * 0.6, 4)
