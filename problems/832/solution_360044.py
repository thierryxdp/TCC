import math

def eh_quadrada(matrizes):
    """Função que diz se uma matriz é quadrada ou não."""
    """List -> Boolean"""
    raiz = math.sqrt(len(matrizes))
    if raiz % 1 == 0:
        return True
    else:
        return False