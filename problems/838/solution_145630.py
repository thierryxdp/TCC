import math

def num_bombons(dinheiro, preco):
    '''
    funcao que define o maior numero de bombons que Pedrinho pode 
    comprar
    :param dinheiro: float
    :param preco: float
    :return: int
    '''
    
    return math.floor(dinheiro/preco)