from random import randint
for i in range(10):
    x = randint(1, 101)
    if x % 2 == 0:
        print(f"{x} is toggle")
    else:
        print(f"{x} is single")

i = 0
while i < 10:
    x = randint(1, 100)
    if x % 2 == 0:
        print(f"{x} is toggle")
    else:
        print("{x} is single")
    i += 1
