n = 1000

def series(k):
    tot = 0
    for i in range(k):
        tot += i * (i+1)
    return tot

square_sum = ((n * (n+1))/2)**2
sum_square = n**3 + n**2/2 - n/2 - 2 * series(n)
print(square_sum)
print(sum_square)
print(square_sum - sum_square)

#alternative method

print((n**4 - n**2)/4 + (n**3 - n)/6)

