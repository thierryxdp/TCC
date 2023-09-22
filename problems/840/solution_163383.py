def bolos(a,b,c):
    '''Retorna a quantidade de bolos possíveis de serem feitos;
    int, int, int -> int'''
    from math import floor
    return min(floor(a/2),floor(b/3),floor(c/5))