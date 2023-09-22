import math

def carros (pessoas,vagas=5):
    """retoma u numeros de carros necessario para a viagem dado o numero de passageiros"""
    return math.ceil(pessoas/vagas)