from math import*
def carros(pessoas, capacidade=5):
    '''Função que calcula o número de carros de determinada capacidade
    (capacidade) que são necessários para transportar uma determinada
    quantidade de pessoas (pessoas).
    int, int -> int
    '''
    return ceil(pessoas/capacidade)