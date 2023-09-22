import math

def bolos int(farinha, ovo, leite):
    """Função que define a quantidade máxima de bolo que João consegue fazer"""
    return math.min(farinha/2, ovo/3, leite/5)