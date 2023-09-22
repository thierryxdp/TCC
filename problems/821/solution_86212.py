from math import prod
def fatorial(n):
    """Esta é a função que dado um número retorna seu fatorial; int -> int"""
    fatorial = list(range(n,0,-1))
    fatorial_final = math.prod(fatorial)
    return fatorial_final