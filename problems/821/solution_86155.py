# Fatorial

def fatorial(x):
    '''Dado um número x, retorna o seu valor fatorial.
    int -> int'''
    fat = 1
    while x>0:
        fat *= x
        x-=1
    return fat