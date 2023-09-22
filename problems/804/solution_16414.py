#Start your python function here
def filtra_pares(array):
    result = []
    for i in (len(array) - 1): 
        if array[i] % 2 == 0:
            result += array[i]            
    return result