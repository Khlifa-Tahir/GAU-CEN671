import numpy as np
import matplotlib.pyplot as plt
import math

def griewank_function(x):

    x = np.array(x)
    idx=np.arange(len(x)).reshape(-1,1)+1 ## counting indices and reshape for multply

    result= np.sum(x**2,axis=-1)/4000 - np.prod(np.cos(x/np.sqrt(idx)),axis=-1)+1
    
    return result


# --- Example Usage ---

if __name__ == "__main__":

    # 1. Setup parameters from the table
    dimension = 30
    search_range = [-500, 500]
    f_min = 0

    # 2. Generate a random input vector within the range [-500, 500]
    # (This simulates a candidate solution in an optimization algorithm)
    population = np.random.uniform(search_range[0], search_range[1], dimension)
    print(f"Input Vector (shape): {population.shape}")
    test_val = [[0.2, 0.6, 1.6],[1,1,2],[1,1,3]] 
    print(f"Input Vector (shape): {test_val}")



    # 3. Calculate the value
    fitness_value = griewank_function(test_val)
    print(f"Function Value: {np.float64(fitness_value)}")

    print(f"Product of :\n {np.prod((2,2,3),axis=-1)}")
    


    
    # 5. Test with a known point
    # If x = [0.2, -0.2], 
    # floor(0.2+0.5) = floor(0.7) = 0
    # floor(-0.2+0.5) = floor(0.3) = 0
    #test_val = [0.2, 0.6, 1.6] 

    test = np.float64(np.full(3, 1))
    print(f"\n test={test}, function={griewank_function(test)}")

    # Expected: floor(0.7)^2 + floor(1.1)^2 + floor(2.1)^2 = 0 + 1 + 4 = 5
    #print(f"\nTest with {test_val}: {np.float64(Schwefel_function(test_val))} (Expected: 5)")