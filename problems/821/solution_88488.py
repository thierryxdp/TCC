def fatorial(n:int) -> int:
    """Essa função, dada um número, calcula e retorna seu fatorial"""
    i = 0
    numeros = list(range(n+1))[::-1]
    multi = [n,]
    while i < len(numeros)-1:
        multi[0]= multi[0]*numeros[i]
    i += 1
    return multi