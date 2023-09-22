import math

def carros(pessoas, capacidade=5):
    """ Calcula a quantidade de carros nescessarios, a partir do numero de pessoas."""
    return math.ceil (pessoas/capacidade)