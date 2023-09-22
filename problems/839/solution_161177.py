def carros(pessoas,capacidade=5):
    """numero de carros necessários para transportar uma determinada quantidade de pessoas"""
    automoveis = Math.ceil(pessoas/capacidade)
    return automoveis