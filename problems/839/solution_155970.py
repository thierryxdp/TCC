import math
def carros(pessoas, capacidade=5):
    """retorna o numero exato de carros(int, int->int)"""
    veiculos= math.ceil(pessoas/capacidade)
    return veiculos