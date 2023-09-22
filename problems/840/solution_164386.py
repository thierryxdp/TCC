import math
def bolos(farinha,ovos,leite):
    """Calcula a quantidade máxima de bolos possiveis com o ingredientes disponiveis"""
    return math.ceil(farinha*2+ovos*3+leite*5)/30