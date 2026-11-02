import numpy as np
import matplotlib.pyplot as plt

def rosenbrock_function(x):

    
    x1=np.vstack((x[1:],x[0]))
    #print("x1=\n",x1) 


    x = np.array(x) 
    x1 = np.array(x1) 
   
    z=100*(x1-x)**2+(x-1)**2
    #print("z=\n",z)   
    result = np.sum(z,axis=-1)   
    return result




# --- Example Usage ---

if __name__ == "__main__":

    # 1. Setup parameters from the table
    dimension = 30
    SN=100
    search_range = [-30, 30]
    f_min = 0

    # 2. Generate a random input vector within the range [-100, 100]
    # (This simulates a candidate solution in an optimization algorithm)
    random_input = np.random.uniform(search_range[0], search_range[1], size=(SN,dimension))
    print("input Random=",random_input.shape)
    #print(f"Input Vector: {random_input[0]}")
    fitness_value = rosenbrock_function(random_input)  
    print("Fitness Random=",(fitness_value))


    # Input_unif=np.array([[1,1,1],[1,1,1],[1,1,1],[1,1,1]])
    # print("Input Uniform=",(Input_unif.shape))
    # # 3. Calculate the value
    # fitness_value = rosenbrock_function(Input_unif)      
    # print(f"Fitness Uniform: {fitness_value}")
    print("-------------------------------------")
    
    test_val = [[0.2, 0.6, 1.6],[1,1,2],[1,1,3]]
    # Expected: floor(0.7)^2 + floor(1.1)^2 + floor(2.1)^2 = 0 + 1 + 4 = 5
    print(f"\nTest with: {test_val}. result:{rosenbrock_function(test_val)} ")