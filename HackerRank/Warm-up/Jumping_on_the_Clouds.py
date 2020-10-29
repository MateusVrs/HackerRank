n = int(input())
c = list(map(int, input().split()))
i, r = 0, c.count(0)-1
while i < len(c)-1:
    if 1 not in c[i:i+3] and len(c[i:i+3]) == 3:
        i += 1
        r -= 1
    i += 1
print(r)
