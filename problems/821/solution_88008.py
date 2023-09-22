def fatorial(x):
    """função para calcular o fatorial de um determinado numero; inti-->int"""
    n=0
    fatorial=1
    c=1
    while fatorial<n:
        fatorial=(n*c)+c
        c=c+1
        return fatorial