t = int(input())
r = ['NO' for v in range(t)]
for v in range(t):
    s1 = input()
    s2 = input()
    for e in s1:
        if e in s2:
            r[v] = 'YES'
            break
for e in r:
    print(e)
