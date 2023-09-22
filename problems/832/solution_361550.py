import math
def eh_quadrada(x):
    elemen = 0
    for i in x:
        if(isinstance(i, int)):
            elemen += 1
        else:
            elemen += len(i)
        
    return isinstance(math.sqrt(elemen), int)