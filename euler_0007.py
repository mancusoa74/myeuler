import math
k = 105000

num = list(n+1 for n in range(k))
num[0] = 0

def remove_multiple(n):
    for i in range(2*n - 1, k, n):
        num[i] = 0

#Sieve_of_Eratosthenes
for i in range(int(math.sqrt(k))+1):
    if num[i+1] != 0:
        remove_multiple(num[i+1])


print(list(filter(lambda n: n>0, num))[10000])


