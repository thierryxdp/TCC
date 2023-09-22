def faltante(L):
    '''dada uma lista com N-1 inteiros numerados de 1 a n, retorna qual inteiro deste intervalo está faltando;
    list --> int'''
    prox=1
    list.sort(L)
    while prox in L:
        prox=prox+1
    return prox