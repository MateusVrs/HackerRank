T = int(input())
r = 0
for t in range(0, T):
    n = input()
    l = list(map(int, input().split()))
    for p in range(len(l)):
        if (l[p]-1) - p >= 3:
            r = 'Too chaotic'
            break
        for i in l[max(0, l[p]-2):p]:
            if i > l[p]:
                r += 1
    print(r)
    r = 0
