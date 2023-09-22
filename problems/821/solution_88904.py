def fatorial (n):
    """Retorna o fatorial de um número n dado como entrada. int-> int"""
    i = n
    fatorial = 0
    while i > 0:
        fatorial = n*(n-1)
        i = i-1
    return fatorial