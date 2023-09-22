def maiores(L,n):
    list.append(L,n)
    list.sort(L)
    indice=list.index(L,n)
    return L[indice+1:]

def acima_da_media(lista): 
    '''   '''
    list.sort(lista) #ordeno
    media=sum(lista)/len(lista) #tem que arredondar?
    lista1=maiores(lista,media)
    if media in lista:
        
        return lista1 
    if media not in lista:
        return lista1