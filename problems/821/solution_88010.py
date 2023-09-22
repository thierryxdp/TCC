def fatorial(x):
    """função para calcular o fatorial de um determinado numero; inti-->int"""
    n=0
    fatorial=1
    while fatorial<x:
        fatorial=(n*x)+x
        n+=1
        fatorial+=1
        return fatorial