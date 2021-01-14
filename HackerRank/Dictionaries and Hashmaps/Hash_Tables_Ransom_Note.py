from collections import Counter
m, n = map(int, input().split())
mw = input().split()
nw = input().split()
r = dict(Counter(nw) - Counter(mw))
print('No' if len(r) != 0 else 'Yes')
