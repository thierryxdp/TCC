from math import ceil
def carros(pessoas, capacidade_veiculos=5):
    '''Recebe a quantidade de pessoas que vão viajar e a capacidade dos veículos (considerando como 5 caso não seja informado) e retorna a quantida de veículos necessários para a viagem; int, int -> int'''
    return ceil(pessoas / capacidade_veiculos)