def carros(pessoas,capacidade=5):
    """Determinar o número exatos de carros para esta viagem;
    int, int -> int"""
    return math.ceil(pessoas/capacidade)