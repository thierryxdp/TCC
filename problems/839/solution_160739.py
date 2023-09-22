import math
def carros (p, c=5):
    """retorna a quantidade de carros necessários para uma determinada viagem dados os números p de pessoas e c de capacidade do carro"""
    return math.ceil(p/c)