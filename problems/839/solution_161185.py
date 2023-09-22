def carros(pessoas,capacidade=5):
    """numero de carros necessários para transportar uma determinada quantidade de pessoas"""
    import math
    automoveis= math.ceil(pessoas/capacidade)
    return automoveis