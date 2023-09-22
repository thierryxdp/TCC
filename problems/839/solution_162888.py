import math
def carros(pessoas, capacidade=5):
    """Calcula o numero de carros necessarios para fazer uma viagem dados os numeros de pessoas e a capacidade do carro"""
    return math.ceil(pessoas/capacidade)