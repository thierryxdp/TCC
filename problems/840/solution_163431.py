from math import floor
def bolos(a,b,c):
    '''Calcula e retorna a quantidade máxima de bolos dados o ingredientes;
    float, float, float -> int'''
    return floor((a + b +c) / 10)