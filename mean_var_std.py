import numpy as np

def calculate(list):

    #Raises a ValueError if the received list doesn't contain exacly 9 elements 
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    #Transforms a list into a 3 x 3 matrix
    tridimentionalArray = np.array(list).reshape(3, 3)
    
    #Mean calculation
    mean_axis_1 = tridimentionalArray.mean(axis=0).tolist()
    mean_axis_2 = tridimentionalArray.mean(axis=1).tolist()
    mean_flattened = tridimentionalArray.flatten().mean().item()
    mean_array = [mean_axis_1, mean_axis_2, mean_flattened]
    
    #Variance calculation
    var_axis_1 = tridimentionalArray.var(axis=0).tolist()
    var_axis_2 = tridimentionalArray.var(axis=1).tolist()
    var_flattened = tridimentionalArray.var().item()
    variance_array = [var_axis_1, var_axis_2, var_flattened]
    
    #Standard deviation calculation
    std_axis_1 = tridimentionalArray.std(axis=0).tolist()
    std_axis_2 = tridimentionalArray.std(axis=1).tolist()
    std_flattened = tridimentionalArray.std().item()
    standard_deviation_array = [std_axis_1, std_axis_2, std_flattened]
    
    #Max calculation
    max_axis_1 = tridimentionalArray.max(axis=0).tolist()
    max_axis_2 = tridimentionalArray.max(axis=1).tolist()
    max_flattened = tridimentionalArray.max().item()
    max_array = [max_axis_1, max_axis_2, max_flattened]

    #Min calculation
    min_axis_1 = tridimentionalArray.min(axis=0).tolist()
    min_axis_2 = tridimentionalArray.min(axis=1).tolist()
    min_flattened = tridimentionalArray.min().item()
    min_array = [min_axis_1, min_axis_2, min_flattened]
    
    #Sum calculation
    sum_axis_1 = tridimentionalArray.sum(axis=0).tolist()
    sum_axis_2 = tridimentionalArray.sum(axis=1).tolist()
    sum_flattened = tridimentionalArray.sum().item()
    sum_array = [sum_axis_1, sum_axis_2, sum_flattened]
    
    #returned dictionary
    return {
        "mean": mean_array,
        "variance": variance_array,
        "standard deviation": standard_deviation_array,
        "max": max_array,
        "min": min_array,
        "sum": sum_array
    }