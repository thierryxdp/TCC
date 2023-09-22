import math

def carros (pessoas,capacidade):
    
    if capacidade:
        return math.ceil(pessoas/capacidade)
    return math.ceil(pessoas/5)