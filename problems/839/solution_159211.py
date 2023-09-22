import math

def carros(p,c=5):
    """retorna o numero de carros nescessário para um viagem dado as pessoas"""
    return math.ceil(p/c)