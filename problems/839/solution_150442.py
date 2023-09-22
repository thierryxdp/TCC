import math

def carros(pessoas, capacidade=5):
    """calcula quantos carros serão necessários para transportar
    um determinado número de pessoas, considerando o valor default
    de capacidade como 5"""
    return math.ceil(pessoas/capacidade)