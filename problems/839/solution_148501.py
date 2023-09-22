def carros(passageiros):
    """Calcula o número de viagens será possível fazer
    dados o número de passageiros."""
    import math
    return math.ceil(passageiros/5)