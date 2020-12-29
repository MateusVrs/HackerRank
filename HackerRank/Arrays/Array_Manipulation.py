#Second attempt
'''
n, m = list(map(int, input().split()))
abk, num = [], list(map(lambda x: 0, list(range(n))))
for v in range(m):
    abk.append(list(map(int, input().split())))
for l in abk:
    for p in range(l[0], l[1]+1):
        num[p-1] += l[2]
print(max(num))
'''

#Third attempt
n, m = map(int, (input().split()))
zero = [0 for i in range(n+1)]
for i in range(m):
    a, b, k = map(int, input().split())
    zero[a-1] += k
    zero[b] -= k
for p in range(len(zero)-1):
    zero[p+1] += zero[p]
print(max(zero[:-1]))
