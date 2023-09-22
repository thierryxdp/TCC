import math
def carros(x, y=5):
    """calcula o numero de carros necessários para levar 'x' pessoas e 'y' vagas em cada carro"""
    return math.ceil(x/y)