import math
def carros(passageiros,capacidade=5):
    carros=passageiros/capacidade
    return math.ceil(carros)