n = int(input())
l = list(map(int, input().split()))
r = 0
for p in range(n):
    while l[p] != p+1:
        x = int(l[p])
        l[p] = l[x-1]
        l[x-1] = x
        r += 1
print(r)
