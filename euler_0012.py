import math
import time

start = time.time()
k = 500

def triangle(n):
    return int(n*(n+1)/2)

def num_divisor(n):
    i = 1
    c = 0
    while i <= math.sqrt(n):
        if (n % i == 0):  
            if (n / i == i):
                c += 1
            else:
                c += 2
        i = i + 1
    return c

t = 1        
while True:
    triang_val = triangle(t)
    if num_divisor(triang_val) > k:
        print(triang_val)
        break
    t += 1

end = time.time()
print(end-start)

