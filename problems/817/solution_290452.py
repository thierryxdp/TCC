def acima_da_media(lista):
    '''   '''
    list.sort(lista)
    media=sum(lista)/len(lista)
    if media in lista:
        indice=list.index(lista,media)
        return lista[indice:]