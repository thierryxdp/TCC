import math
def carros (passageiros=5,carros):
    """calcular o numero de carros para uma certa quantidade de passageiros"""
    return math.ceil (passageiros//carros)