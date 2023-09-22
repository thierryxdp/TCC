def fatorial(numero):
    """funcao que calcula o fatorial do numero de entrada;
    int -> int"""
    fatorial=1
    n=0
    while n<numero:
        fatorial=fatorial*(numero-n)
        n=n+1
    return fatorial