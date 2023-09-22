from math import ceil
def carros(num_pessoas: int, cap_veiculo: int = 5) -> int:
    return ceil(num_pessoas/cap_veiculo)