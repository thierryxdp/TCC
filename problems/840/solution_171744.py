import math
from math import trunc

def bolos(A,B,C):
    
    bolo = min(A/2,B/3,C/5)
    
    return math.trunc(bolo)