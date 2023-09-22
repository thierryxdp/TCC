import math
def carros(passageiros, capacidade=5):
    """ Retorna a quantidade de carros"""
    return math.ceil (passageiros/capacidade)