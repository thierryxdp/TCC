def faltante(ListaL):
    '''funcao que retorna o numero inteiro x que pertence
    ao intervalo [1,N] mas que não pertence a lista de
    entrada L'''
    list.sort(ListaL)
    f=0
    g=1
    while f<len(ListaL):
        if ListaL[f]==g:
            g=g+1
        f=f+1
    return g