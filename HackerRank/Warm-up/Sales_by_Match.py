def sockMerchant(n, ar):
    r = 0
    ar_set = set(ar)
    for element in ar_set:
        n_sock = ar.count(element)
        while n_sock > 0:
            n_sock -= 2
            if n_sock >= 0:
                r += 1
    return r


n = int(input())
ar = list(map(int, input().rstrip().split()))
print(sockMerchant(n, ar))
