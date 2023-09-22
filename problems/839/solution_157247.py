import math;
def carros(qtd_pessoas, capacidade_v):
    ''' Retorna a quantidade de veículos necessários para transportar um grupo de amigos,
    dados (qtd_pessoas) quantidade de integrantes e (capacidade_v) capacidade dos veículos.
    int, int -> int
    '''
    return math.ceil(mqtd_pessoas / capacidade_v);