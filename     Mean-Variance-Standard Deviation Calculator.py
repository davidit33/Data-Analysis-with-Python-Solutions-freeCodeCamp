import numpy as np

def calculate(list):
  if len(list) != 9:
     raise ValueError("List must contain nine numbers.")
  else:
    np_arr = np.array(list)
    np_arr = np.reshape(np_arr, (3,3))
    arr_flatten = np_arr.flatten()  
    #mean
    mean_0 = np.mean(np_arr, axis=0)
    mean_1 = np.mean(np_arr, axis=1)
    mean_f = np.mean(arr_flatten)
    #variance
    var_0 = np.var(np_arr, axis=0)
    var_1 = np.var(np_arr, axis=1)
    var_f = np.var(arr_flatten)
    #desvaiation
    std_0 = np.std(np_arr, axis=0)
    std_1 = np.std(np_arr, axis=1)
    std_f = np.std(arr_flatten)
    #max
    max_0 = np.max(np_arr, axis=0)
    max_1 = np.max(np_arr, axis=1)
    max_f = np.max(arr_flatten)
    #min
    min_0 = np.min(np_arr, axis=0)
    min_1 = np.min(np_arr, axis=1)
    min_f = np.min(arr_flatten)
    #sum
    sum_0 = np.sum(np_arr, axis=0)
    sum_1 = np.sum(np_arr, axis=1)
    sum_f = np.sum(arr_flatten)

    calculations = {
    'mean': [mean_0.tolist(), mean_1.tolist(), mean_f],
    'variance': [var_0.tolist(), var_1.tolist(), var_f],
    'standard deviation': [std_0.tolist(), std_1.tolist(), std_f],
    'max': [max_0.tolist(), max_1.tolist(), max_f],
    'min': [min_0.tolist(),min_1.tolist(),min_f],
    'sum': [sum_0.tolist(), sum_1.tolist(), sum_f]
    }

    return calculations