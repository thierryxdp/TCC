def fatorial(n):
    """comentário"""
    fatorial = n
    i = 0
    numeros = list(range(n+1))
    while i < len(numeros):
        fatorial = fatorial*numeros[i]
    i = i + 1
    return fatorial