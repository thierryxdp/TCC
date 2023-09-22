def acima_da_media(lista):
    L=lista
    M=sum(L)/len(L)
    L+[M]
    list.sort(L)
    
    return L