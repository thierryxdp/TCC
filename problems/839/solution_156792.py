def carros(pessoas,capacidade=5):
    """Numeros de carros necessario para realizar a viagem"""
    automoveis = math.ceil(pessoas / capacidade)
    return automoveis