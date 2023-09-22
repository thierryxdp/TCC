import math
def bolos (A,B,C):
    numero1 = math.ceil(A/2)
    numero2 = math.ceil(B/3)
    numero3 = math.ceil (C/5)
    
    return min (numero1,numero2,numero3)