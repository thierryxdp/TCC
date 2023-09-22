from math import ceil 
def carros(pessoas,capacidade=5):
    """ função que calcula o número de carros necessários para a viagem"""
    return ceil (pessoas/capacidade)