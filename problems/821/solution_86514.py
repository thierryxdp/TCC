def fatorial(f):
    """funcao que calcula o fatorial dado um numero de entrada.
    int -> int"""
    fatorial = 1
    while f > 0:
       fatorial = fatorial * f
       f = f - 1
    if f <0:
        fatorial = 'indefinido'
    return fatorial