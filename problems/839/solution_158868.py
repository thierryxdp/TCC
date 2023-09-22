import math
def carros (pessoas,carros=5):
    """funcao que define a quantidade exata de veiculos necessarios para a viagem"""
    return math.ceil(pessoas/carros)