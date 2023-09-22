import math
carros(p,c=5):
    """Calcula o numero de carros necessarios para determinada viagem de acordo com o numero de pessoas"""
    return math.ceil(p/c)