def maiores(L,n):
    list.append(L,n)
    list.sort(L)
    indice=list.index(L,n)
    return L[indice+1:]

def acima_da_media(lista):
    '''   '''
    list.sort(lista) #ordeno
    media=sum(lista)/len(lista)
    lista1=maiores(lista,media)
    if media in lista:
        indice=list.index(lista,media) #indice da média
        return lista1 #fatiamento