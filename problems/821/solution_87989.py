def fatorial(x):
    """função para calcular o fatorial de um determinado numero; inti-->int"""
    fatorial=1
    a=1
    while fatorial<x:
        fatorial=(x*a)+a
        a+=1
    return fatorial