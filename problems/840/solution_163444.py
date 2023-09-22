import math
def bolos(a,b,c):
    '''Calcula e retorna a quantidade máxima de bolos dados o ingredientes;
    int, int, int -> int'''
    a//=2
    b//=3
    c//=5
    qntd_bolos = min(a,min(b,c))
    return qntd_bolos