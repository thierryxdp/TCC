def fatorial(n):
    """Retorna o fatorial do numero n"""
    i = 1
    f = n
    while (n-i)>0:
        f = f*(n-i)
        i = i + 1
    return f