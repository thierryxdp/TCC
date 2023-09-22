import math
def carros(p,c=5):
    """retorna o número de carros necessários a uma viagem com base no número de pessoas p e na capacidade do carro c. Se a capacidade  não for convencional, deve-se informa-la
    int,int--->int"""
    return math.floor(p/c)