'''
n = list(map(lambda x: False, range(int(input()))))
l = list(map(int, input().split()))
r, m, p, t = 0, 0, 0, []
for v in range(len(l)):
    if n[p] == False and l[p] != p+1:
        n[p] = True
        t.append(p)
        p = l[p]-1
        r += 1
        if p in t:
            m -= 1
            if n.count(False) == 0:
                break
            p = n.index(False)
            t.clear()
    elif n[p] == False and l[p] == p+1:
        n[p] = True
        if n.count(False) == 0:
            break
        p = n.index(False)

print(r+m if m != 0 else r-1)
'''

# 2 3 4 1 5

# Second Attempt
n = list(map(lambda x: False, range(int(input()))))
l = list(map(int, input().split()))
r = 0

print(r)
