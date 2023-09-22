from math import ceil

def carros(p,c=5):
    '''Calcula e retorna a quantidade de carros necessários para uma viagem dados
    p = número de pessoas que vão na viagem e c = capacidade de pessoas por veículo.
    Caso não seja dada a capacidade de pessoas por veículo, c = 5.
    Só aceita valores positivos para p e c.
    int, int -> int'''
    return ceil(p/c)