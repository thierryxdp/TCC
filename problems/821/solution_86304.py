def fatorial(n):
    """Retorna o fatorial do numero n.int-->int"""
    numero=1
    limite=int(n)
    while numero!=limite:
        n=n*(numero)
        numero=numero+1
    return n