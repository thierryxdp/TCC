#Exercicio 2
import math
from math import ceil 

def carros (pessoas,capacidade=5):
    '''calcula numero de carros necessarios para x pessoas.
        Se preferir, dar a capacidade maxima, senao assumido 5'''
    carros = math.ceil(pessoas/capacidade)
    return carros;