import math

import random


points=[(1,2),(3,4),(5,6),(7,8)]
k=2
print(points[:k])

x0=[p[0] for p in points]
x = sum(x0)

print("Sum of x-coordinates:", x0)

z=0

clusters = [[] for _ in range(k)]
print(clusters)
# for _ in range(k):
#     z=z+1
#     print(z)

#------------------------------
search_space=[-5, -3, -1, 0, 1, 3, 5]
def random_solution():
    return random.choice(search_space)


print("\nRandom solution:", random_solution())

rnsol=[random_solution() for _ in range(4)]
print("Random solutions:", rnsol)
