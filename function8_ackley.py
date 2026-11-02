import numpy as np
import matplotlib.pyplot as plt
import math

def ackley_function(x):
    x = np.array(x)
    result= -20*np.exp(-0.2*np.sqrt(np.sum(x**2,axis=-1)/len(x)))-np.exp(np.sum(np.cos(2*np.pi*x),axis=-1)/len(x))+20+np.e
    
    return result


# ============================================= Test function ============================

if __name__ == "__main__":

    # 1. Setup parameters from the table
    dimension = 30
    search_range = [-32, 32]

    # 2. Generate a random input vector within the range [-500, 500]
    # (This simulates a candidate solution in an optimization algorithm)
    population = np.random.uniform(search_range[0], search_range[1], dimension)
    print(f"Input Vector (shape): {population.shape}")
    test_val = [[0.2, 0.6, 1.6],[1,1,2],[1,1,3]] 
    print(f"Input Vector (shape): {test_val}")


    # 3. Calculate the value
    fitness_value = ackley_function(test_val)
    print(f"Function Value: {np.float64(fitness_value)}")

    print(f"Nutural number e :\n {np.e}")

    test = np.float64(np.full(3, 1))
    print(f"\n test={test}, function={ackley_function(test)}")
