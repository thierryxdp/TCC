import math

def carros (n_pessoas, n_capacidade=5):
    return math.ceil(n_pessoas//n_capacidade)