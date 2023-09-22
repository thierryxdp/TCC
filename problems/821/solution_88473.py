def fatorial(n:int) -> int:
    """Essa função, dada um número, calcula e retorna seu fatorial"""
    i = 0
    numeros = list(range(n+1))[::-1]
    multi = [n]
    while i > len(numeros)-1:
        multi = [multi[0]*multi[i],]
    i += 1
    return multi[0]