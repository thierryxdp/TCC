def fatorial(numero):
    '''Funcao que calcula o fatorial do numero dado
    int -> int'''
    f = 1
    i = 1
    while i<=numero:
        f = f * i
        i = i + 1
    return f