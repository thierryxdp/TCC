from numpy import prod

def fatorial(num):
    """..."""
    lista = list(range(num,0,-1))
    resultado = prod(lista)
    
    return resultado