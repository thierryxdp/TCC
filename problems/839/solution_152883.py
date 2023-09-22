import math
def carros (carros=5, passageiros):
    """calcular o numero de carros para uma certa quantidade de passageiros"""
    return math.ceil (carros//passageiros)