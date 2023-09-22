import math
def eh_quadrada(x):
    elemen = 0
    for i in x:
        elemen += len(i)
    return isinstance(math.sqrt(elemen), int)