def carros(pessoas, capacidade=5):
    """Calcula quantos carros são necessarios dado um numero de pessoas.
       int, int -> float"""
    from math import *
    return math.ceil(pessoas//capacidade)