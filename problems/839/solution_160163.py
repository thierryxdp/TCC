from math import*
def quant_carros(passageiros,capacidade=5):
    carros=passageiros/capacidade
    return ceil(carros)