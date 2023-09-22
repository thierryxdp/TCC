import math
def num_bombons(d,pb):
    '''Retorna o máximo de bombons que podem ser comprados;
    Onde d é o dinheiro, e pb é o preço do bombom'''
    return max(d/pb)