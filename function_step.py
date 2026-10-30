import numpy as np
import matplotlib.pyplot as plt

def step_function(x):
    """   
    Parameters:
    x : array-like
        Input vector or matrix of shape (D,) or (N, D).
        
    Returns:
    float
        The sum of the squared rounded values.
    """
    x = np.array(x)

    
    rounded_x = np.floor(x + 0.5)

    
    result = np.sum(rounded_x**2)


   
    return result




# --- Example Usage ---

if __name__ == "__main__":

    # 1. Setup parameters from the table
    dimension = 30
    search_range = [-100, 100]
    f_min = 0

    # 2. Generate a random input vector within the range [-100, 100]
    # (This simulates a candidate solution in an optimization algorithm)
    random_input = np.random.uniform(search_range[0], search_range[1], dimension)

    # 3. Calculate the value
    fitness_value = step_function(random_input)

    print(f"Dimension: {dimension}")
    print(f"Input Vector (first 5 elements): {random_input[:5]}")
    print(f"Function Value: {fitness_value}")

    # 4. Test with the global minimum (should be 0)
    global_min_input = np.zeros(dimension)  # Input is all zeros
    print(f"\nValue at Global Minimum (0,0,...): {step_function(global_min_input)}")

    # 5. Test with a known point
    # If x = [0.2, -0.2], 
    # floor(0.2+0.5) = floor(0.7) = 0
    # floor(-0.2+0.5) = floor(0.3) = 0
    test_val = [0.2, 0.6, 1.6] 
    # Expected: floor(0.7)^2 + floor(1.1)^2 + floor(2.1)^2 = 0 + 1 + 4 = 5
    print(f"\nTest with {test_val}: {step_function(test_val)} (Expected: 5)")