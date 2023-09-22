def fatorial(n):
    """Funcao calcula e retorna o fatorial de um numero(n)
    int,int->int"""
    n=()
    fatorial=1
    c=1
    while fatorial<len(n):
        fatorial=fatorial*c+c
        c=c+1
    return fatorial