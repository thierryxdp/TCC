from math import *
def carros(passageiros,capacidade=5):
    """dados o número de passageiros a serem transportados, e, se diferente de 5, a capacidade dos carros disponíveis, calcula quantos carros serão necessários para que todos viajem"""
    return math.ceil(passageiros/capacidade)