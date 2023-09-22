def carros(pessoas,capacidade=5):
    """Determinar o número exatos de carros para esta viagem"""
    return math.ceil(pessoas/capacidade)