import math
def bolos(A,B,C):
    '''Função que retorna a quantidade de bolos que João
    consegue fazer
    int,int,int->int'''
    return math.trunc((A*2+B*3+C*5)/10)