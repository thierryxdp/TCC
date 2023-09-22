from math import ceil

def carros(pessoas,capacidade=5):
    '''retorna a quantidade de carros necessários para realizar um viagem'''
    return ceil(pessoas // capacidade)