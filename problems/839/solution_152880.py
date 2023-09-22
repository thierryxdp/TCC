import math
def carros (carros, passageiros=5):
    """calcular o numero de carros para uma certa quantidade de passageiros"""
    return math.ceil (carros//passageiros)