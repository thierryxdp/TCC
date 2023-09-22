def fatorial(n):
    """Funcao calcula e retorna o fatorial de um numero(n)
    int,int->int"""
    fatorial=1
    c=1
    while fatorial<n:
        fatorial=n*c+c
        c=c+1
    return fatorial