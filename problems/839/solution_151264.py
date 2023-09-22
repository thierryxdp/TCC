from math import ceil
def carros(x,z=5):
    ''' funcao recebe x e z, onde x e a quantidade de pessoas e z quantidade de passageiro por carros'''
    return ceil( x//z)