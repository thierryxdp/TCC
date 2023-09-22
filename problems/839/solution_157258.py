import math;
def carros(qtd_pessoas, capacidade_v = 5):
    ''' Retorna a quantidade de veículos necessários para transportar um grupo de amigos,
    dados (qtd_pessoas) quantidade de integrantes e (capacidade_v) capacidade dos veículos.
    int, int -> int
    '''
    return math.ceil(qtd_pessoas / capacidade_v);