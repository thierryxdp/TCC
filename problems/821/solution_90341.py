def fatorial(n):
    """Funcao que recebe um numero n e retorna o fatorial dele. int=>int"""
    x=n
    fatorial=1
    while x>1:
        fatorial=fatorial*n*(n-1)
        x=x-2
    return fatorial