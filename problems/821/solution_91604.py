def fatorial(numero):
    """ retorna o fatorial de um numero dado
    como valor de entrada.
    int -> int"""
    i = 1
    fatorial = 1
    while i <= numero:
        fatorial = fatorial * i
        i += 1
    return fatorial