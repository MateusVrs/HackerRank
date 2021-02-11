t = int(input())
r = [0 for n in range(t)]
for v in range(t):
    s, d = input(), dict()
    pi, pf, n = 0, 0, 1
    while True:
        s1 = sorted(s[pi:pf+n])
        if ''.join(s1) not in d:
            d[''.join(s1)] = 1
        else:
            d[''.join(s1)] += 1
        pi += 1
        pf += 1
        if pf+n > len(s):
            pi = pf = 0
            n += 1
        if n == len(s):
            break
    for k in dict(d):
        if d[k] == 1:
            del d[k]
    for i in d.items():
        r[v] += (i[1]*(i[1]-1))/2
for e in r:
    print(int(e))
