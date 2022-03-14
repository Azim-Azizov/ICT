n = int(input())
t = []
for i in range(n):
    t.append([i])
# print(t)
for i in range(n):
    k = []
    for j in range(1+i, i + n*(n-1) + 2, n):
        k += [j]
    t[i] = k
    print(k)
print(*t, sep="\n")
