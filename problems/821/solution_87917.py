def fatorial(numero:int) -> int:
    """Dado um número, a função calcula o fatorial dele."""
    i = 0
    numeros = list(range(numero+1))[2:]
    fatorial = 1
    
    while i < len(numeros):
        fatorial = fatorial * numeros[i]
        i += 1
        
    return fatorial