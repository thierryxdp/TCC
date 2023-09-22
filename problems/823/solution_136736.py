def faltante(l):
    """função que dada uma lista com N - 1 inteiros numerados de 1 a N,
    descubra qual número inteiro deste intervalo esta faltando.
    list -> list"""
    i = 1
    recente = 1
    while i in l:
        if i in l:
            i = recente
            recente = recente + 1
    return i