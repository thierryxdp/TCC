from math import floor

def num_bombons(dinheiro: float, preco_bombom: float) -> int:
    return int(floor(dinheiro/preco_bombom))