import math
def carros(P,c=5):
    """Calcula o número de carros necessários para viagem dado o número 
    de pessoas P"""
    return math.ceil(P/c)