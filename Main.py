from math import log2
def anti_primes(k):
    if k == 2: return 2;
    a = [0] * (k + 1)
    for i in range(2, int(k ** 0.5)):
        for j in range(i ** 2, k + 1, i):         
            a[j] += 1
    p=a[:(int)(log2(k)) + 1: -1].index(max(a))
    return k - p
