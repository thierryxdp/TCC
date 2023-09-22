import math
def carros(pessoas,capacidade=5):
    """calcula a quantidade de veiculos necessarios para transportar dado numero de pessoas, carros e capacidade dos mesmos. Se a capacidade do carro for diferente de 5, digite-a"""
    carros = math.ceil(pessoas/capacidade)
    return carros