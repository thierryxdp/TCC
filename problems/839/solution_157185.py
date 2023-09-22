def carros (pessoas,capacidade):
    """calcula o número exato de carros para
    o número de pessoas"""
    automoveis = math.ceil (pessoas / capacidade)
    return automoveis