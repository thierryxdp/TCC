import math
from math import ceil
def carros(p,c=5):
 #Numero de carros necessario para transportar determinada quantidade de pessoas
    N=p/c
    return math.ceil(N)