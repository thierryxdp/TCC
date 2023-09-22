from math import gcd
def bolos(a,b,c):
    '''Calcula e retorna a quantidade máxima de bolos dados o ingredientes;
    int, int, int -> int'''
    return gcd(a,b,c)