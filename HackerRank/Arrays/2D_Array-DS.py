array, sums = [], []
for r in range(0, 6):
    array.append(list(map(int, input().split())))
for h in range(0, 4):
    for p in range(0, 4):
        sums.append(sum(array[h][p:p+3]) + array[h+1]
                    [p+1] + sum(array[h+2][p:p+3]))
print(max(sums))
