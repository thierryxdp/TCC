from math import *
def carros(pessoas,capacidade=5):
    """calcula o número de carros necessários, tendo o número de pessoas e a capacidade do carro"""
    return math.ceil(pessoas/capacidade)