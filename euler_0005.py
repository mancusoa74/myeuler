from functools import reduce

k=20
factors = [1, ]
num = [n+1 for n in range(k)]

for i in range(k):
    current_factor = num[i]
    for j in reversed(range(i)):
        division, reminder = divmod(current_factor, factors[j])
        current_factor = division if reminder == 0 else current_factor
    factors.append(current_factor)

print(reduce((lambda x,y:x*y),factors))
