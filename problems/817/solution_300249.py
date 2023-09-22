def acima_da_media(L):
    '''
       Funcao que recebe uma lista e retorna uma lista ordenada
       list -> list
    '''
    L = sorted(L)
    L1 = L.index(L)
    return L[L1::]