from math import *
def carros(pessoas,capacidade=5):
    """Dadas a quantidade de pessoas, e a capacidade dos veículos(todos iguais), retornar a quantidade de carros necessários
    int,int->int"""
    return ceil(pessoas/capacidade)