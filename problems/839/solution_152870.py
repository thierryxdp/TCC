import math
def numero_de_carros (carros, passageiros=5):
    """calcular o numero de carros para uma certa quantidade de passageiros"""
    return math.ceil (passageiros//carros)