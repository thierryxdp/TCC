import math
def carros(num_pessoas, capacidade = 5):
    '''Calcula o número exato de carros necessários
    para uma viagem, dados o número de pessoas e a 
    capacidade dos veículos;
    int, int -> int'''
    return math.ceil(num_pessoas/capacidade)