def carros(pessoas):
    """Numeros de carros necessario para realizar a viagem"""
    automoveis = math.ceil(pessoas / 5)
    return automoveis