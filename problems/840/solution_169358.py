import math
def bolos(A,B,C):
    '''
       funcao que retorna o numero de bolos que joao 
       consegue fazer a partir da quantidade de ingredientes
       que ele possui
       int, int -> int
    '''
    quantidade = min(A/2,B/3,C/5)
    return math.floor(quantidade)