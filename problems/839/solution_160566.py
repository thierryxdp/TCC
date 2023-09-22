from math import ceil

def carros(N,C=5):
    '''funcao que calcula o numero de carros necessarios para uma viagem dados a
    quantidade de pessoas (N) e a capacidade dos carros(C)'''
    return math.ceil(C/N)