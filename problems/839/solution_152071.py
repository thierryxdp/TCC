import math
def carros (pessoas,capacidade=5):
    quantidade = pessoas/capacidade
    
    return math.ceil(quantidade)

def outros_veiculos(pessoas,capacidade):
    quantidade = pessoas/capacidade
    
    return math.ceil(quantidade)