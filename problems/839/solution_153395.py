from math import ceil
def carros(passageiros,carros=5):
    return ceil((passageiros*carros)/carros**2)