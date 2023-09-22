import math
def carros(passageiros,capacidade=5):
    """Função que retorna o número de carros necessários para uma viagem dados o número de passageiros e sua capacidade."""
    return math.ceil(passageiros/capacidade)