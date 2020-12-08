#Second attempt
n, m = list(map(int, input().split()))
abk, num = [], list(map(lambda x: 0, list(range(n))))
for v in range(m):
    abk.append(list(map(int, input().split())))
for l in abk:
    for p in range(l[0], l[1]+1):
        num[p-1] += l[2]
print(max(num))
