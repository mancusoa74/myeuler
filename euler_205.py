import itertools as it
from collections import defaultdict

pyr_tot = 262144
pyramid_dict = defaultdict(int)
items_p = it.product((1,2,3,4), repeat=9)
for item in items_p:
     pyramid_dict[sum(item)] += (1/pyr_tot)
print(pyramid_dict)

print("---------")
cub_tot = 46656
cubic_dict = defaultdict(int)
items_c = it.product((1,2,3,4,5,6), repeat=6)
for item in items_c:
     cubic_dict[sum(item)] += (1/cub_tot)
print(cubic_dict)
