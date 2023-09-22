import math
def carros(p,c=5):
    """função que determina e retorna quantos carros de capacidade c são necessários em uma viagem com p pessoas"""
    return (math.ceil(p//c))