target = 10
print(sum(list(map(lambda x: x if (x%3 == 0 or x%5 == 0) else 0, range(target)))))
##
##def SumDivBy(target, n):
##    p = int(target / n)
##    return int(n*(p * (p+1))/2)
##
##print(SumDivBy(target-1,3)+SumDivBy(target-1,5)-SumDivBy(target-1,15))
