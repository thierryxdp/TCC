import math

def carros(passageiros,capacidade=5):
    """calcula a quantidade de carros necessária para transportar os passageiros"""
    return math.ceil(passageiros/capacidade)