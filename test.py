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


population=[(0,3),(0,1),(1.5,1),(2,2),(2,1),(3,2)]

def Dist(p1,p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

print("Distance between points:", [Dist(population[1],d)for d in population])


total_distance=[]
for i in range(len(population)):
    
    fi=sum([Dist(population[i],d)/len(population) for d in population])

    fi=round(fi,3)
    print("\n fi=",fi)
    total_distance.append(fi)

print(">>>",total_distance)