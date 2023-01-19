from math import log, sqrt, cos

def function_to_find_root(x):
    """
    A function that takes an input x and returns 2*x-cos(x)
    
    Parameters:
        x (float): The input value
        
    Returns:
        float: 2*x-cos(x)
    """
    return 2*x-cos(x)

def dichotomie(function_to_find_root, left_interval, right_interval, tolerance, max_iterations):
    """
    A function that finds the root of a given function using bisection method.
    
    Parameters:
        function_to_find_root (function): The function for which the root needs to be found.
        left_interval (float): The left end of the interval in which the root is supposed to be.
        right_interval (float): The right end of the interval in which the root is supposed to be.
        tolerance (float): The desired precision of the root approximation.
        max_iterations (int): The maximum number of iterations to perform before giving up.
    
    Returns:
        tuple: A tuple containing the root of the function and the value of the function at that root.
    """
    if function_to_find_root(left_interval)*function_to_find_root(right_interval) > 0:
        print("Function does not have a root in the given range")
        return None
    iteration_count = 0
    while abs(left_interval-right_interval) > tolerance and iteration_count <= max_iterations:
        middle_point = (left_interval + right_interval)/2
        if function_to_find_root(middle_point) == 0:
            return middle_point, function_to_find_root(middle_point)
        if function_to_find_root(middle_point)*function_to_find_root(left_interval) < 0:
            right_interval = middle_point
        else:
            left_interval = middle_point
        iteration_count += 1
    return middle_point, function_to_find_root(middle_point)

root, function_val = dichotomie(function_to_find_root, 0, 0.5, pow(10, -3), 100)
print(root, function_val)
