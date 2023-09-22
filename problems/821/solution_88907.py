def fatorial (n):
    """Retorna o fatorial de um número n dado como entrada. int-> int"""
    i = n +1 
    fatorial = 0
    while i > 0:
        fatorial = n*(n-i)
        i = i-1
    return fatorial