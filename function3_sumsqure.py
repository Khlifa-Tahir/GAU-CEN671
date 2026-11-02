import numpy as np
import matplotlib.pyplot as plt

def sumsqure_function(x):
     
    x = np.array(x) 
    idxx=np.arange(len(x)).reshape(-1,1)+1 ## counting indices and reshape for multply

    #print(">>>idx=",idx)
    # b=x+1
    # c=x**2*idx

    # print("c=",c.shape)
    #print("x=\n",x)   
    #z=x**2*idx
    #print("z=\n",z)   
    result = np.sum(x**2*idxx,axis=-1)   
    return result




# --- Example Usage ---

if __name__ == "__main__":

    # 1. Setup parameters from the table
    dimension = 3
    SN=2
    search_range = [-10, 10]
    f_min = 0

    # 2. Generate a random input vector within the range [-100, 100]
    # (This simulates a candidate solution in an optimization algorithm)
    random_input = np.random.uniform(search_range[0], search_range[1], size=(SN,dimension))
    print("input Random=",random_input.shape)
    #print(f"Input Vector: {random_input[0]}")
    fitness_value = sumsqure_function(random_input)  
    print("Fitness Random=",(fitness_value))


    # Input_unif=np.array([[1,1,1],[1,1,1],[1,1,1],[1,1,1]])
    # print("Input Uniform=",(Input_unif.shape))
    # # 3. Calculate the value
    # fitness_value = sumsqure_function(Input_unif)      
    # print(f"Fitness Uniform: {fitness_value}")
    print("-------------------------------------")
    
    test_val = [[0.2, 0.6, 1.6],[1,1,2],[1,1,3]]
    # Expected: floor(0.7)^2 + floor(1.1)^2 + floor(2.1)^2 = 0 + 1 + 4 = 5
    print(f"\nTest with: {test_val}. result:{sumsqure_function(test_val)} ")