from math import *
def carros(n,p=5):
    '''Calcula o número de pessoas (n) para o número de passageiros que o carro possui capacidade (p)'''
    return ceil(n/p)