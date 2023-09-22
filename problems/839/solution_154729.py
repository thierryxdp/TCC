import math

def carros(p,v=5):
    """função que determina a quantidade de carros necessarios
    com base no numero de lanches
    int, int-> int"""
    return math.ceil(p/v)