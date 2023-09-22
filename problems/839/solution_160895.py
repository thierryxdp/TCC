from math import *
def carros(pessoas,capacidade=5):
    """calcula o numero de carros necessarios para transportar uma quantidade de pessoas, dada a capacidade do veiculo. Caso a capacidade nao seja informada, sera atribuido o valor igual a 5"""
    return ceil(pessoas/capacidade)