import math

def carros (pessoas,vagas=5):
    """retoma u numeros de carros necessario para a viagen dado o numero de passageiros"""
    return ceil(pessoas//vagas)