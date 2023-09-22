from math import ceil
def carros(pessoas, capacidade=5):
    '''funcao que calcula quantos carros seriam necessarios para realizar uma viagem com tantas pessoas; int int->int'''
    return ceil(pessoas/capacidade)