def carros(pessoas,vagas=5):
    '''Calcula e retorna o números de carros necessários para um número dado de pessoas e vagas no carro;
    int, int -> int'''
    from math import ceil
    return ceil(pessoas/vagas)