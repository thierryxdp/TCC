import math
def carros(P,c=5):
    """Calcula o número de carros necessários para viagem dados o número 
    de pessoas P e se a capacidade de transporte do veículo não for 
    convencional c"""
    return math.ceil(P/c)