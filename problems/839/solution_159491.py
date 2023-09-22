import math

def carros(pessoas,capacidade=5):
    "Retorna exatamente quantos carros serão necessários para a viagem dado a quantidade de pessoas e a capacidade do veículo"
    return math.ceil(pessoas/capacidade)