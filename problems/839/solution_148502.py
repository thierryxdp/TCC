def carros(passageiros, pessoas=5):
    """Calcula o número de viagens será possível fazer
    dados o número de passageiros."""
    import math
    return math.ceil(passageiros/pessoas)