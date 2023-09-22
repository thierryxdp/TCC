from math import ceil
def carros(pessoas,capacidade=5):
    '''Calcula o numero de cargas nescessarios para transportar	certas quantidade de pessoas a partir da quantidade de pessoas
    int->float'''
    return ceil(pessoas/capacidade)