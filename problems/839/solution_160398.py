import math
def carros(num_pássageiros, capacidade_carro=5):
    return math.ceil(num_pássageiros/capacidade_carro)