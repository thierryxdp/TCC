def faltante(L):
    '''Função que analisa e aponta qual dos inteiros dados
    na lista como parâmetro está faltando.
    list -> int'''
    i=0
    L.sort()
    while i<len(L):
        if L[i]-L[i-1]>1:
            L[i]-1
        i=i+1
    return L