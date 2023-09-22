import math
def carros(pessoas,capacidade=5):
    "retorna a quantidade de carros que será necessário para transportar o número de pessoas. Se a capacidade do carro não for dado capacidade assume 5"""
    return math.ceil(pessoas/capacidade)