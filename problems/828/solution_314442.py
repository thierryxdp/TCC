import math

def primo(numero):
    '''comentario padra
    e1, e2 -> s'''
    for i in range(2, math.ceil(numero/2)+1):
        if numero % i == 0:
            return False
    return True