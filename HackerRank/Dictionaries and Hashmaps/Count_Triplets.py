from collections import Counter
n, r = map(int, input().split())
arr = list(map(int, input().split()))
right = Counter(arr)
left = Counter()
result = 0

for e in arr:
    right[e] -= 1
    if e % r == 0:
        if e/r in left and e*r in right:
            result += left[e/r]*right[e*r]
    left[e] += 1

print(abs(result))
