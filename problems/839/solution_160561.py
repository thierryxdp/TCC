import math
def carros(pessoas,capacidade=5):
    """calcula o numero de carros necessarios em relacao ao numero de pessoas dividindo pessoas pela capacidade que a principio e igual a cinco; int,int->int"""
    carrosnum = math.ceil(pessoas / capacidade)
    return carrosnum