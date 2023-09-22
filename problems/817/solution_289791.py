def media(lista):
    return sum(lista)//len(lista)
def acima_da_media(lista):
    L=lista
    list.insert(L,media(lista),1)
    L.sort()
    k=list.index(L,media(lista)) 
    return L[k+1: ]