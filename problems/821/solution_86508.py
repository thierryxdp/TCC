def fatorial (num):
    """Funcao que recebe um número e calcula o fatoral
    int-->int"""
    i=1
    fatorial=1
    while i<=num:
        fatorial=fatorial*i
        i=i+1
    return fatorial