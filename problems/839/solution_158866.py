import math
def carros(carros=5,pessoas):
    """funcao que define a quantidade exata de veiculos necessarios para a viagem"""
    return math.ceil(pessoas/carros)