import math

def carros(p, z=5):
    """Retorna o numero de carros necessarios para fazer uma viagem, dado o numero de pessoas.
       int => int"""
    return math.ceil(p/z)