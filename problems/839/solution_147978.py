import math

def carros (pessoas):
    """retoma u numeros de carros necessario para a viagem dado o numero de passageiros"""
    return math.ceil(pessoas/5)