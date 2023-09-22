def fatorial(x):
    """função para calcular o fatorial de um determinado numero; inti-->int"""
    fatorial=0
    a=0
    while fatorial<x:
        fatorial=(x*a)+a
        a+=1
    return fatorial