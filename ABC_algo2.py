from pprint import pp
import random
import math
import numpy as np
from function_step import step_function


# -------------------------
# Problem functions   (from paper formulas)
# -------------------------


def objective(x):
#     # cost to minimize (same toy problem)
     return  step_function([x])  # minimize this



def fitness_from_cost(cost):
    # Eq.(4) style transform: fitness = 1 / (1 + cost)
    return 1.0 / (1.0 + cost)


# def clamp_to_search_space(value):
#     # map continuous candidate to nearest discrete allowed value
#     #print("value:", value)
#     #exit()
#     nearest = min(search_space, key=lambda s: abs(s - value))
#     return nearest



def produce_neighbor(population, i_index):
    """
    Produce candidate v using document formula:
    v_j = z_ij + phi_j * (z_ij - z_kj)
    Here we have 1D positions, so j is implicit.
    - pick k != i randomly
    - phi in [-1, 1]
    """
    # choose k different from i_index
    indices = list(range(len(population)))
    indices.remove(i_index)
    k = random.choice(indices)
    z_i_val = population[i_index]
    z_k_val = population[k]
    phi = random.uniform(-1.0, 1.0)  # phi_j in [-1,1]
    v = z_i_val + phi * (z_i_val - z_k_val)

    # clamp to continuous bounds then map to discrete search space
    #if v < Z_MIN: v = Z_MIN
    #if v > Z_MAX: v = Z_MAX
    return v
    #return clamp_to_search_space(v)




def scout_random_solution():
    # document's scout formula: z = Zmin + rand(0,1)*(Zmax - Zmin)
    val = Z_MIN + random.random() * (Z_MAX - Z_MIN)
    return val
    #return clamp_to_search_space(val)





# -------------------------
# ABC algorithm (document style)
# -------------------------
def abc_document_style(
    SN=4,        # number of food sources = number of employed bees
    population=None,  # initial population of food sources (candidate solutions)
    MCN=None,      # maximum cycle number
    limit=5,     # abandonment limit
    seed=None
):
    if seed is not None:
        random.seed(seed)






    # 2. Generate initial population z_i, i = 1..SN
    #population = [scout_random_solution() for _ in range(SN)]

    #print('Initial population:', (population.shape))
    

    #for i in range(len(population)):
        #costs=sum([objective(population[i],d)/len(population) for d in population])
    costs = [objective(z) for z in population]
    
    #print(costs)
    #exit()
    
    fits = [fitness_from_cost(c) for c in costs]

    trial = [0] * SN  # abandonment counters [0, 0, 0, 0]

    

    

    # memorize best
    best_idx = min(range(SN), key=lambda i: costs[i])
    
    best_solution = population[best_idx]
    best_cost = costs[best_idx]

    print(f"Initial best solution: {best_solution}, cost: {best_cost}")

    

    cycle = 1
    while cycle <= MCN:
        # 6. Employed bees phase
        for i in range(SN):
            candidate = produce_neighbor(population, i)
            cand_cost = objective(candidate)
            # greedy selection
            if cand_cost <= costs[i]:
                population[i] = candidate
                costs[i] = cand_cost
                fits[i] = fitness_from_cost(cand_cost)
                trial[i] = 0
            else:
                trial[i] += 1

        # 7. Calculate probability values p_i for solutions z_i by fitness
        total_fit = sum(fits)
        if total_fit == 0:
            probs = [1.0 / SN] * SN
        else:
            probs = [f / total_fit for f in fits]


        #---------------------------------------------------------
        # 8. Onlooker bees phase
        # number of onlookers commonly equals SN
        for _ in range(SN):
            # roulette wheel selection based on probs
            r = random.random()
            accum = 0.0
            selected = 0
            for idx, p in enumerate(probs):
                accum += p
                if r <= accum:
                    selected = idx
                    break

            candidate = produce_neighbor(population, selected)
            cand_cost = objective(candidate)
            
            if cand_cost <= costs[selected]:
                population[selected] = candidate
                costs[selected] = cand_cost
                fits[selected] = fitness_from_cost(cand_cost)
                trial[selected] = 0
            else:
                trial[selected] += 1



        #---------------------------------------------------------

        # 9. Scout phase: replace abandoned solutions
        for i in range(SN):
            if trial[i] >= limit:
                population[i] = scout_random_solution()
                costs[i] = objective(population[i])
                fits[i] = fitness_from_cost(costs[i])
                trial[i] = 0

        # 10. Memorize best solution so far
        current_best_idx = min(range(SN), key=lambda i: costs[i])
        if costs[current_best_idx] < best_cost:
            best_cost = costs[current_best_idx]
            best_solution = population[current_best_idx]

        # optional: print progress
        print(f"Cycle {cycle}: best = {best_solution}, cost = {best_cost}, population = {population}")

        cycle += 1

    return {
        "best_solution": best_solution,
        "best_cost": best_cost,
        "population": population,
        "costs": costs,
        "fits": fits
    }

# -------------------------
# Run the modified ABC
# -------------------------
if __name__ == "__main__":

    # 1. Setup parameters from the table
    dimension = 3
    SN = 4  # number of bees (population size)
    search_space= [-100, 100]

    # continuous bounds derived from search_space
    Z_MIN = min(search_space)
    Z_MAX = max(search_space)

    MCN=10 # maximum cycle number

    best_value = float('inf')  # initialize best value to infinity
    best = None                # initialize best solution
    stopNoImprv=[0]            # for tracking best values over iterations
    n0_improvement = 0         # counter for improvements

    #-------------------------------------------------------

    # 2. Generate a random input vector within the range [-100, 100]
        # (This simulates a candidate solution in an optimization algorithm)
    bees = np.random.uniform(search_space[0], search_space[1], size=(SN, dimension))# size of the bees array (Ns, dimension)

    

    result = abc_document_style(SN=4,population=bees, MCN=10, limit=3, seed=123)

    print("Best solution:", result["best_solution"], "cost:", result["best_cost"])
    print("Final population:", result["population"])
    print("Final costs:", result["costs"])
    print("Final fitnesses:", result["fits"])
