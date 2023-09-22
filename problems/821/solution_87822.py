def fatorial(n):
    """Funcao calcula e retorna o fatorial de um numero(n)
    int,int->int"""
    fatorial=1
    while n>=1:
        fatorial=fatorial*n
        n=n-1
    return fatorial