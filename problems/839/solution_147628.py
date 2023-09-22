import math
def carros(pessoas,capacidade=5):
    """Esta função calcula o numero de carros necessarios para x quantiades de pessoas para fazer uma viagem"""
    return math.ceil(pessoas/capacidade)