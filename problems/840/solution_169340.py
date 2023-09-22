import math
def bolos(A,B,C):
    '''
       funcao que define a quantidade maxima de bolos 
       que joao pode fazer de acordo com a quantidade
       que possui de farinha A, ovos B e leite C.
       int, int -> int
    '''
    return math.floor((2*A+3*B+5*C)/10)