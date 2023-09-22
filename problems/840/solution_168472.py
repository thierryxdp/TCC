import math
def bolos (farinha,ovos,leite):
    """função que determina qual a quantidade máxima de bolobs que se pode fazer a partir dos ingredientes e do que se faz necessário na receita"""
    return min(math.floor(farinha/2)+math.floor(ovos/3)+math.floor(leite/5))