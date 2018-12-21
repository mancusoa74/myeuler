import itertools as it

#brute force - very ugly

abc = it.product(range(1000), range(1000), range(1000))

for i in abc:
    a = i[0]
    b = i[1]
    c = i[2]
    if (a+b+c == 1000 and a>0 and b>0 and c>0 and a<b and b<c and (a**2+b**2) == c**2):
        print("{} ({})=({})".format(i, (a**2+b**2), c**2))
        break

print("done")    
