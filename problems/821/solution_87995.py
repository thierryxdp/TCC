def fatorial(x):
    """função para calcular o fatorial de um determinado numero; inti-->int"""
    a=0
    fatorial=0
    while fatorial<x:
        fatorial=(x*a)
        a+=1
    return (x*fatorial(x-1))