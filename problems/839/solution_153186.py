import math
def carros(P,C=5):
    """retorno o valor necessário de veiculos para um número x de pessoas"""
    return math.ceil(P/C)