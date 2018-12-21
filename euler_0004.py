import itertools as it

def is_palindromic(n):
    num = str(n)
    digits = len(num)
    for i in range(digits):
        if num[i] != num[digits-i-1]:
            return False
    return True
    

max_range = 1000
prod_size = max_range**2


prod = list(it.product(list(range(max_range)), repeat=2))
prod.reverse()

a = []
for i in prod:
    nprod = i[0] * i[1]
    if is_palindromic(nprod):
        a.append(nprod)
        #print("{}x{}={}".format(i[0], i[1], nprod))
        #break

print(max(a))

