x, y, z = map(int, input("range by spaces").split(" ")+[0])
print(sum(map(lambda x : x ** 2, range(x, y + 1))))