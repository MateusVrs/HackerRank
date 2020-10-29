from math import floor
s = input()
n = int(input())
count_a = s.count('a')
k1 = floor(n/len(s))
r = count_a*k1
cut_s = s[:round((n/len(s)-k1)*len(s))].count('a')
print(cut_s+r)
