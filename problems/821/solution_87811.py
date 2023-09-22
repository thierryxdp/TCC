def fatorial(n):
    """Funcao calcula e retorna o fatorial de um numero(n)
    int,int->int"""
    fatorial=1
    c=1
    while fatorial<n:
        fatorial=n*(n-1)*(n-2)*(n-3)*(n-4)*(n-5)*(n-6)*(n-7)
    return fatorial