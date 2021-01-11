n, m = map(int, input().split())
zero = [0 for i in range(n+1)]
for v in range(m):
    a, b, k = map(int, input().split())
    zero[a-1] += k
    zero[b] += -k
zero = list(filter(lambda x: x != 0, zero))
for p in range(len(zero)-1):
    zero[p+1] += zero[p]
print(max(zero[:-1]))
