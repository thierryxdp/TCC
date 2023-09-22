import math
def carros(num_pessoas, capacidade = 5):
    num_carros = math.round(num_pessoas/capacidade)
    return num_carros