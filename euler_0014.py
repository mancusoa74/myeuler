import math
import time

start = time.time()
global c
c = 0
def collatz(n):
    global c
    c += 1
    #print(n)
    if n > 1:
        if n % 2 == 0:
            collatz(n//2)
        else:
            collatz(3*n+1)

k = 1000000
chain = 0
value = 0

def factor(n):
    exp = 0
    for i in range(int(math.log(n, 2))):
        if n % (2**(i+1)) == 0:
            exp += 1
    prime = n / (2**exp)
    return exp, int(prime)



def num_collatz(m):
    items = 1
    prime = 0
    n = m
    while prime != 1:
        if n %2 == 0:
            items += 1
            exp, prime = factor(n)
            #print("#{} {}".format(exp, prime))
            n = prime
        else:
            items += 1
            exp, prime = factor(3*n + 1)
            #print("!{} {}".format(exp, prime))
            items += exp
            n = prime
    return items
      
##for i in range(k-1):
##    curr_chain = num_collatz(i+1)
##    #print("{} -> {}".format(i, curr_chain)) 
##    if curr_chain > chain:
##        chain = curr_chain
##        value = i+1
##    if i % 100000 == 0:
##        print(i)
##
##
##print("{} -> {}".format(value, chain))

##for i in range(k):
##    collatz(i)
##    if c > chain:
##        chain = c
##        value = i
##    c = 0
##    if i % 100000 == 0:
##        print(i)
##
##print("{} -> {}".format(value, chain))

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
##
##
##for i in reversed(range(1, 1000000)):
##    if isPrime(i) != 0:
##        collatz(i)
##        #print("{} -> {}".format(i, c))
##        if c > chain:
##            chain = c
##            value = i
##        if i % 100000 == 0:
##            print(i)
##        c = 0
##
##print("{} -> {}".format(value, chain))

##collatz(9)
end = time.time()
print(end-start)
        
print(isPrime(837799))
#soluzione: 837799 --> 525



        
