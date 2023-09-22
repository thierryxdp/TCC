def carros(pessoas,capacidade=5):
    """calcular a capacidade de carros necessários na viagem"""
    return math.ceil(pessoas/capacidade)