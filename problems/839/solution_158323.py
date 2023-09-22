import math

def carros(qnt_pessoas,capacidade_carro, n_carros):
    int(qnt_pessoas)
    int(capacidade_carro)
    n_carros=qnt_pessoas/capacidade_carro
    return math.ceil(n_carros)