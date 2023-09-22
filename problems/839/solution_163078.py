def carros(passageiros, capacidade=5):
    """Funcao que retorna o numero de carros necessarios"""
    import math
    return math.ceil(passageiros/capacidade)