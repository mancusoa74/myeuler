import time
start = time.time()

##def fib(n):
##    if n <= 2:
##        return n
##    return fib(n-2) + fib(n-1)
##
##print(list(map(fib, range(34))))


fib = [1,2]
i = 0
while True:
    add = fib[i] + fib[i+1]
    if add > 4000000:
        break
    fib.append(add)
    i += 1

print(sum([item for item in fib if item %2 == 0]))

end = time.time()
print(1000 * (end - start))

