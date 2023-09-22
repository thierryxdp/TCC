#Start your python function here
def filtra_pares(array):
    result = []
    for i in range(len(array) - 1): 
        if array[i] % 2 == 0:
            result.append(array[i])    
    return tuple(result)