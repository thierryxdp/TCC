#Exercicio 2
import math
from math import ceil 

def carros (pessoas,capacidade=5):
    carros = math.ceil(pessoas/capacidade)
    return carros;