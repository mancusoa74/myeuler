def firstPrime(z):
    t=2
    while ((t*t) <= z):
        if z%t == 0:
            return t
        t +=1
    return z

def factors(n):
    a = []
    f = firstPrime(n)
    m = n
    while m > 1:
        a.append(f)
        m = int(m / f)
        f = firstPrime(m)
    return a



print(max(factors(600851475143)))
