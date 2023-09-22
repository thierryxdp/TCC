import math
def carros(pessoas,capacidade=5):
    """calcula o número de carros necessários para uma viagem dado o número
    de pessoas; caso o veículo não seja convencional sua capacidade será 
    informada também
    int, int -> int"""
    return math.ceil(pessoas/capacidade)