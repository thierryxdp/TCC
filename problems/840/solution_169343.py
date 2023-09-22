import math
def bolos(A,B,C):
    '''
       funcao que retorna o numero de bolos que joao 
       consegue fazer a partir da quantidade de ingredientes
       que ele possui
       int, int -> int
    '''
bolos = math.floor((A/2+B/3+C/5)/3))
     return bolos