import math
def eh_quadrada(x):
    elemen = 0
    for i in x:
        elemen += max(1, len(i))
    if(x == []):
        elemen += 1
    return math.sqrt(elemen)