from pprint import pp
import argparse
import random
import matplotlib.pyplot as plt
import numpy as np
from function1_step import step_function
from function2_sphere import sphere_function
from function3_sumsqure import sumsqure_function
from function4_rosenbrock import rosenbrock_function
from function5_rastrigin import rastrigin_function
from function6_schwefel import Schwefel_function
from function7_griewank import griewank_function
from function8_ackley import ackley_function



# -------------------------
# Algorithm functions   (from paper formulas)
# # -------------------------


def objective(x): 
    
    return  func_name(x)


def fitness_from_cost(cost):
    # Eq.(4) style transform: fitness = 1 / (1 + cost)
    #ranks = np.argsort(np.argsort(cost))  # 0 = best
    #return 1/(1+ranks)
    return 1/(1+cost)


def produce_neighbor(population, i_index):
    
    # choose k different from i_index
    indices = list(range(len(population))) ### len(population) is SN (number of bees)
    #print("indices:", indices)
    indices.remove(i_index)
    k = random.choice(indices)

    z_i_val = population[i_index]
    z_k_val = population[k]
    
    phi = np.random.uniform(-1.0, 1.0, size=len(population[0]) )  # phi_j in [-1,1] (demin, ) for 3D
    
    v = z_i_val + phi * (z_i_val - z_k_val)
    # print("z_i_val:", z_i_val.shape)
    # print("z_k_val:", z_k_val.shape)
    # print("phi:", phi.shape)
    # print("v:", v.shape)    
    # exit()
    # clamp to continuous bounds then map to discrete search space
    #if v < Z_MIN: v = Z_MIN
    #if v > Z_MAX: v = Z_MAX
    return v


def scout_random_solution(dimension):
    # scout formula: z = Zmin + rand(0,1)*(Zmax - Zmin)
    newsol = np.random.uniform(0, 1, size=dimension) * np.array([Z_MAX - Z_MIN]).reshape(1,-1)  # for 3D

    #print("Scout random solution:", newsol.shape)
    #exit()
    return newsol
#===================================================================================
    




# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<   ABC algorithm  >>>>>>>>>>>>>>>>>>> 

def ABC_Optim_Algo(
    SN=None,        # number of food sources = number of employed bees
    population=None,  # initial population of food sources (candidate solutions)
    MCN=None,      # maximum cycle number
    limit=None,     # abandonment limit
    seed=None
):
    
    if seed is not None:
        random.seed(seed)
        np.random.seed(seed)
   
   

    costs=objective(population)  ## for initial solution
     #print('costs=',costs)
        
    # fits = [fitness_from_cost(c) for c in costs]   
    fits = fitness_from_cost(costs)
    trial = [0] * SN  # cycle counter for abandonment length on SN, initialized to 0
   
    # print("Initial fitnesses:", fits)
    # print("Initial trial counters:", (trial))
    # exit()    

    # memorize best solution so far

    best_idx = min(range(SN), key=lambda i: costs[i]) 
    best_solution = population[best_idx]
    best_cost = costs[best_idx]

    #print(f"len of Initial best solution: {len(best_solution)}, cost: {best_cost}")
    cycle = 1
    runcost = [0] * (MCN )  # store best cost at each cycle

    while cycle <= MCN:

        #print("cycle=",cycle)
        #---------------------------------------------------------


        # 6. Employed bee phase: Number SN                
        for i in range(SN):
            # print("-----------------------")
            # print('i=',i)
            candidate = produce_neighbor(population, i).reshape(1,dimension)
            # print("cand_ employ",candidate.shape)           
            cand_cost = objective(candidate).item()  ## to extract to scalar
            # print("cand_cost employ",(cand_cost))

            current_best_idx = max(range(SN), key=lambda i: costs[i])

            # greedy selection ==============================
            if cand_cost <= costs[current_best_idx]:
                #print("true: candi_cost",cand_cost)
                population[current_best_idx] = candidate
                costs[current_best_idx] = cand_cost
                fits[current_best_idx] = fitness_from_cost(cand_cost)
                trial[i] = 0    #  abandon to replace nectar finesh
            else:
                #print("false: candi_cost",cand_cost)
                trial[i] += 1   # stay more cycle
            
            #print("costs after",costs)
        #exit()



        # 7. Calculate probability values p_i for solutions z_i by fitness
        total_fit = sum(fits)
        if total_fit == 0:
            probs = [1.0 / SN] * SN  ## always == 1          
        else:
            probs = [f / total_fit for f in fits]


        #---------------------------------------------------------
        # 8. Onlooker bee phase:  Number SN 
        
        for j in range(SN): ## for each probs (float)

            # print("+++++++++++++++++++++++++++++++")
            # print("j=",j)

            # selection based on probs
            r = random.random()  ## level to follow a dancing activity
            # to avoid stucking at local minima. Randomness allow for
            # exploration. worse solution may lead to global optima eventuall
            accum = 0.0 # the accumulated probability
            selected = 0
            # print("random level",r)
            # print("total porbs",np.float64(probs))
            for idx, p in enumerate(probs):
                accum += p                
                # print("idx=",idx)
                # print("porbs",p)
                # print("accum=",accum)          

                if r <= accum:
                    selected = idx  # accumulate untill find solu. idx
                    # which makes condition true
                    break

            candidate = produce_neighbor(population, selected).reshape(1,dimension)

            # print("cand onlooker",candidate.shape)            
            cand_cost = objective(candidate).item()
            # print("cand_cost onlooker",cand_cost)
            
            if cand_cost <= costs[selected]:
                population[selected] = candidate
                costs[selected] = cand_cost
                fits[selected] = fitness_from_cost(cand_cost)
                trial[selected] = 0   # replace nectar finish (leave)
            else:
                trial[selected] += 1  # stay still nectar (wait)

        #exit()
        # e.g. >> trial=[ 3,2,0,1,0] for SN=5
        #---------------------------------------------------------
       
        # 9. Scout bee phase: replace abandoned solutions
        for i in range(SN):
            # print("==================================")
            # print("jj=",i)
            if trial[i] >= limit:                
                # this generates a new random solution for the abandoned food source
                # print("all population",population)
                # print("scout popul[i] before:", population[i])
                #population[i] = scout_random_solution(population.shape[1]) 
                population[i] = scout_random_solution(dimension)
                #population[i]=population[i].reshape(1,dimension) 
                # print("all population",population)
                # print("scout popul after:",population[i])
                
                costs[i] = objective(population[i]).item()                
                fits[i] = fitness_from_cost(costs[i])
                trial[i] = 0
                


        # 10. Memorize best solution so far
        current_best_idx = min(range(SN), key=lambda i: costs[i])
        if costs[current_best_idx] < best_cost:
            best_cost = costs[current_best_idx]
            best_solution = population[current_best_idx]
        
        runcost[cycle-1] = best_cost
        cycle += 1       
        

    return {
        "best_solution": best_solution,
        "best_cost": best_cost,
        "population": population,
        "costs": costs,
        "fits": fits,
        "runcost": runcost
    }
#--------------------------------------------------------------------------------------






# -------------------------
# Run  ----------------------  Artifitial Bee Colony  ----------------------------
# -------------------------


if __name__ == "__main__":



    parser= argparse.ArgumentParser(description=" Run ABC Algorithm")
    #parser2= argparse.ArgumentParser(description=" Dimension Number")


    parser.add_argument(
        "--function", type=str, default='Step',
        choices=["Step","Sphere","SumSquare","Rosenbrock","Rastrigin","Schwefel","Griewank","Ackley"],
        help="Name of used test function" )

    parser.add_argument(
        "--Dimension", type=int, default=3,
        # choices=["1","2","3"],
        help="Dimension Number")

    parser.add_argument(
            "--SN", type=int, default=3,
            #choices=["20","30","3"],
            help="Solution Number")

    parser.add_argument(
                "--MCN",  type=int, default=10,
                #choices=["20000","200","300"],
                help="Max Cycle Number")


    parser.add_argument(
                    "--Range", type=float, default=10.0,
                    #choices=["10","5.12","30","32","500","600"],
                    help="Range")

    args=parser.parse_args()

    
    Function_Map={"Step":step_function,
                  "Sphere":sphere_function,
                  "SumSquare":sumsqure_function,
                 "Rosenbrock":rosenbrock_function,
                 "Rastrigin":rastrigin_function,
                 "Schwefel":Schwefel_function,
                 "Griewank":griewank_function,
                 "Ackley":ackley_function}
    func_name=Function_Map[args.function]
    


    # 1. Setup parameters from the table

    MCN= args.MCN         # maximum cycle number    
    dimension = args.Dimension
    SN = args.SN          # number of bees (population size)
    search_space= [-args.Range , args.Range]      # continuous search space bounds

    #exit()

    limit = SN*300               # to simulate waiting time on one solu       
    Z_MIN = min(search_space)      # continuous bounds derived from search_space
    Z_MAX = max(search_space)

    

    #-------------------------------------------------------

    # 2. Generate  initial population z_i, i = 1..SN...random input vector within the range [-100, 100]
    # (This simulates a candidate solution in an optimization algorithm) size of the bees array (Ns, dimension)
   
    bees = np.random.uniform(search_space[0], search_space[1], size=(SN, dimension))
    

    result = ABC_Optim_Algo(SN=SN,population=bees, MCN=MCN, limit=limit, seed=None)

    #print("Best solution:", result["best_solution"], "cost:", result["best_cost"])
    #print("Final population:", result["population"])
    #print("Final costs:", result["costs"])
    print("Final fitnesses:", result["fits"])

    # xx=[float(x) for x in result["runcost"]]
    xx=result["runcost"][-1]
    
print("Final costs:", xx)


figure, ax = plt.subplots()
ax.plot(range(1, MCN + 1), result["runcost"], marker='o')
ax.plot(MCN,xx, marker='o',label=f"Minimum= {xx:.2f}")

ax.set_xlabel('Cycle')  
ax.set_ylabel('Best Cost') 
graph_title = f'{args.function}  function performance.'
ax.set_title(graph_title,fontweight='bold')
ax.text(0.95,0.95,f'MaxCycle={MCN}\nDimension={dimension} \nPopulation={SN} \n|Range|={search_space[1]}',transform=ax.transAxes,verticalalignment='top',horizontalalignment='right',bbox=dict(facecolor='magenta',edgecolor='black'))
ax.grid(True)
ax.legend(loc='lower right',bbox_to_anchor=(1,0.15))
plt.show()
