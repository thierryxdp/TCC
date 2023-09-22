import math

def carros(n_pessoas,carro=5):
    ''' define quantos carros precisam para levar o numero de pessoas fornecido'''
    return math.ceil(n_pessoas/carro)