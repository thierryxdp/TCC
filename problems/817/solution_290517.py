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
    if int(media) in lista1:
        del [0]
        return lista1 
    if int(media) not in lista1:
       
        return lista1