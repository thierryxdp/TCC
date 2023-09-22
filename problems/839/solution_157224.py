def carros (pessoas,capacidade = 5):
    """calcula o número exato de carros para
    o número de pessoas"""
    automoveis = math.ceil(pessoas/capacidade)
    return automoveis