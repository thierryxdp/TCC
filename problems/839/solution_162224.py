from math import*
def carros(pessoas,capacidade=5):
    """calcular o numero de carros necessarios para a viagem"""
    return math.ceil(pessoas/capacidade)