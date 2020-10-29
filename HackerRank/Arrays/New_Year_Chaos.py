T = int(input())
r = 0
for t in range(0, T):
    l = list(range(1, int(input())+1))
    q = list(map(int, input().split()))
    for p in range(len(q)):
        if q[p] - l[p] > 2:
            r = 'Too chaotic'
            break
        for sp in range(max(0, q[p]-2), p):
            if q[sp] > q[p]:
                r += 1
    print(r)
    r = 0
