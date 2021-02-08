import random
from itertools import product, permutations

lower =("abcdefghijklmnopqrstuvwxyz")
Upper = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
Symbols=("!@#$%^&*()_+-={}[]|\"':;?/>.")
Numbers=('1234567890')
light=(lower+Upper+Symbols+Numbers)
print(random.sample(light,k=18))
print(len(list(product(light, range(18)))))

#If you change what k= you can change how many items there are.
