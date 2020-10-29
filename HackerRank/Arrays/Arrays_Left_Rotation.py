n, d = list(map(int, input().split()))
a = list(map(str, input().split()))
new_a = a[:]
for i in range(0, n):
    new_a[i-d] = a[i]
print(' '.join(new_a))
