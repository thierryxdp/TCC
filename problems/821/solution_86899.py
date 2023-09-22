def fatorial(n):
    """Retorna o fatorial do numero n"""
    i = 1
    while (n-i)>0:
        n = n*(n-i)
        i = i + 1
    return n