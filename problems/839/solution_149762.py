import math

def carros(pessoas,capacidade=5):
    """retorna o numero exato de carros necessarios dados o numeor de pessoas e a capacidade do veiculo"""
    return math.ceil(pessoas/capacidade)