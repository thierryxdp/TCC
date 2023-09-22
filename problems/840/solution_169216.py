import math
def (a,b,c) :
    ''' essa função calcula o numero máximo de bolos inteiros que
    joão pode fazer, dado o numero de ingredientes que ele possui'''
    quantidade_minima_f = a/2
    quantidad_minima_o = b/3
    quantidade_minima_l = c/5
    return math.min (quantidade_minima_f, quantidade_minima_o, quantidade_minima_l)