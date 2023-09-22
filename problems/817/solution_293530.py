def acima_da_media(lista):
    L=lista
    M=sum(L)/len(L)
    P=L+[M]
    list.sort(P)
    t=list.index(P,M)
    list.remove(P,M)
    return P[t+1:]