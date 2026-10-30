import random
import numpy as np
import matplotlib.pyplot as plt
from function_step import step_function


# Objective function
def f(x):
    return step_function([x])  # minimize this

#____________________________________________________


 # 1. Setup parameters from the table
dimension = 3
Ns = 100  # number of bees
search_space0 = [-100, 100]
MCN=100

#-------------------------------------------------------


# 2. Generate a random input vector within the range [-100, 100]
    # (This simulates a candidate solution in an optimization algorithm)
bees = np.random.uniform(search_space0[0], search_space0[1], size=(Ns, dimension))


best_value = float('inf')  # initialize best value to infinity
best = None  # initialize best solution
stopNoImprv=[0]
n0_improvement = 0  # counter for improvements


for iteration in range(MCN):  # few simple rounds
    print("\nIteration", iteration + 1)

    # Employed bees phase: try small changes
    for i in range(bees.shape[0]):  # for each bee):
        current = bees[i,:]
        # pick a nearby value randomly

        index = random.randint(0, bees.shape[0] - 1)  # pick a random index for neighbor
        neighbor = bees[index, :]
        #print("-----",index)
        #print(f"Bee {i}: Current {current}, Neighbor {neighbor}, f(Current)={f(current)}, f(Neighbor)={f(neighbor)}")
        #exit()
        if f(neighbor) < f(current):

           # print('check cost',f(neighbor)<f(current))
            bees[i,:] = neighbor  # move to better flower
            #print(f"Bee {i} moved to better flower: {neighbor} with f(x)={f(neighbor)}")
        else:
            #print('check cost',f(neighbor)<f(current))
            bees[i,:] = current  # stay at current flower
            #print(f"Bee {i} stayed at current flower: {current} with f(x)={f(current)}")

#--------------------------------------------------------------------------
    # Onlooker bees phase: choose best solutions # (simplified: pick the best among current bees)

    fitness = np.array([f(b) for b in bees],dtype=float)  # exclude the first bee for fitness calculation
    
    best_idx = np.argmin(fitness)
    #print("Best bee index:", best_idx)
    best_bee = bees[best_idx]
    #print("Best bee this iteration:", best_bee, "with f(x) =", f(best_bee))

    if f(best_bee) < best_value:
        best = f(best_bee)
        best_value = f(best_bee)


#---------------------------------------------------------------------------
    # Scout bee phase: replace worst bee with random new one
    worst_idx = np.argmax(fitness)
    bees = np.delete(bees, worst_idx, axis=0)  # remove the worst bee

    #print("Worst bee index:", worst_idx)
    #print(">>.",bees.shape)
    ppp=np.random.uniform(search_space0[0], search_space0[1], size=(Ns, dimension))
    #print("Random new bee:", ppp.shape)
    bees = np.vstack([bees, ppp])  # add a new random bee

    #print("Bees:", bees)
    print("Best so far:", "with f(x) =", best_value)

    checkt = best_value

    stopNoImprv.append(checkt)

    
    if stopNoImprv[-2] == best_value:
        n0_improvement =n0_improvement + 1  # increment the counter for no improvement
    else:
        n0_improvement =0 

    
    if n0_improvement > 30:  # if no improvement for 10 iterations
        break 
        #print("No improvement for", n0_improvement, "iterations.")


    # if n0_improvement > 10:  # if no improvement for 10 iterations
    #     print("Global minimum found!")
    #     break
    # else:
    #     continue
    #     print("No improvement for", n0_improvement, "iterations.")
print("\nFinal best solution:", best, "with f(x) =", best_value)

figure, ax = plt.subplots()
ax.plot(range(len(stopNoImprv)), stopNoImprv, marker='o')
ax.set_title('Best Value Over Iterations')
ax.set_xlabel('Iteration')
ax.set_ylabel('Best Value')
plt.grid()
plt.show()


