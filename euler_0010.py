import math
import time
start=time.time()
k = 2000000

def isPrime(n):
    if n == 1: return 0
    if n < 4: return n
    if n % 2 == 0: return 0
    if n < 9: return n
    if n % 3 == 0: return 0
    r = math.floor(math.sqrt(n))
    f = 5
    while f <= r:
        if n % f == 0: return 0
        if n % (f + 2) == 0: return 0
        f += 6
    return n


sum_prime = 0
for n in range(k):
    sum_prime += isPrime(n)
elapsed = time.time()-start
print(sum_prime)
print(elapsed)



