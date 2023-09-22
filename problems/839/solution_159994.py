def carros(pessoas, capacidade=5):
    from math import ceil
    num_carros = ceil(pessoas/capacidade)
    return num_carros