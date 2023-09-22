import math

def Carros(qnt_pessoas,capacidade_carro):
    int(qnt_pessoas)
    int(capacidade_carro)
    n_carros=qnt_pessoas/capacidade_carro
    return math.ceil(n_carros)