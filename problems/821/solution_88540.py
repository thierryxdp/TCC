def fatorial(n:int) -> int:
    """Essa função, dada um número, calcula e retorna seu fatorial"""
    i = multi = 1
    numeros = list(range(n+1))[::-1]
  
    while i < len(numeros)-1:
        multi = [multi[i-1]*numeros[i],]
    i += 1
    return multi[0]