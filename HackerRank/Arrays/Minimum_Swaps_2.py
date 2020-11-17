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
n = list(range(int(input())+1))
l = list(map(int, input().split()))
r = p = 0
while len(n) != 1:
    if l[p] != p+1:
        n.remove(p)
        p = l[p]-1
        if p not in n:
            p = min(n)
            r -= 1
        r += 1
    else:
        n.remove(p)
        p = min(n)
print(r)
