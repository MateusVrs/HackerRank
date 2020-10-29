steps = int(input())
path = input()
u = d = x = r = 0
for element in path:
    if element == 'U':
        u += 1
    else:
        d += 1
    if d > u:
        x += 1
    if u == d and x > 0:
        x = 0
        r += 1
print(r)
