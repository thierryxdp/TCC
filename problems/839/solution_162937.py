import math 
def carros (pessoas,capacidade=5):
    veiculos = math.ceil(pessoas / capacidade)
    return veiculos