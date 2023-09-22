import math
def carros (Np,capacidade):
    """Esta função irá calcular o número de carros necessários para uma determinada quantidade de pessoas"""
    carros=Np/capacidade
    return math.ceil(carros)