from math import floor
def bolos(a,b,c):
    '''Calcula e retorna a quantidade máxima de bolos dados o ingredientes;
    float, int, float -> int'''
    return floor((a/2 + b/3 + c/5) / 10)