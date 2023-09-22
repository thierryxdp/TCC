from math import floor
def bolo(farinha,ovo,leite):
    ''' '''
    a = flor(farinha / 2) 
    b = floor(ovo / 3) 
    c = floor(leite / 5)
    minimo = min (a,b,c)
    return minimo