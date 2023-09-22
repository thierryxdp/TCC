def acima_da_media(lista):
    L=lista
    S=sum(L)
    N=len(L)
    Med=S/L 
 
    L+[Med]
    list.sort(L)
    t=list.index(L,Med)
    return L[t+1:]