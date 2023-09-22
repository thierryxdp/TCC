from math import ceil

def carros (passageiros, capacidade=5):
    """calcula uma quantidade de carros necessária para um número de pessoas fazer uma viagem. Caso não seja
 	   informada a capacidade do veículo, será usada a quantidade convencional (5)."""
    return ceil(passageiros/capacidade)