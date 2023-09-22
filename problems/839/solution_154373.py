import math

def carros(p,c=5):
    '''função que recebe o número de pessoas que viajarão(p)
    e divide pela capacidade de passageiros nos bancos do carro(c);
    int,int->int'''
    return math.ceil(p/c)