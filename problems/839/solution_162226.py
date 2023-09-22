def carros(pessoas,capacidade=5):
    import math

    """calcular o numero de carros necessarios para a viagem"""
    return math.ceil(pessoas/capacidade)