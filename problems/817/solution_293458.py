def acima_da_media(lista):
    L=lista
    M=sum(L)/len(L)
    L+[M]
    list.sort(L)
    t=list.index(L,M)
    return L[t+1:]