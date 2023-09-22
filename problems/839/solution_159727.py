import math
def carros(n_pessoas, capacidade=5):
    veiculos= math.ceil(n_pessoas/capacidade)
    return veiculos