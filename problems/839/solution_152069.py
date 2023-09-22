import math
def carros (pessoas):
    quantidade = pessoas/5
    
    return math.ceil(quantidade)

def outros_veiculos(pessoas,capacidade):
    quantidade = pessoas/capacidade
    
    return math.ceil(quantidade)