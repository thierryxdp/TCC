import math
def carros (p,c=5):
    """função que calcula o número de veiculos necessários para certa quantidade de pessoas"""
    return math.ceil(p/c)