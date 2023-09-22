def faltante(l):
    '''função que dada uma lista(l), com N-1 inteiros numerados
    de 1 a N, retorna qual número inteiro deste intervalo está faltando
    list -> int'''
    i = 1
    atual = 1
    while i in l:
        if i in l:
            i = atual
            atual = atual +1
    return i