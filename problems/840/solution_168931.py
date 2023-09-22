import math

def bolos(A, B, C):
    ''' calcula quantos bolos que podem ser feitos a quantidade de variáveis. '''
    resultado = math.floor(2*A , 3*B , 5*C)
    return resultado