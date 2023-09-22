import math
def carros(pessoas,capacidade=5):
    '''Função que calcula e retorna o número exato de carros necessários para a viagem;
    int, int -> int'''
    automoveis = math.ceil(pessoas / capacidade)
    return automoveis