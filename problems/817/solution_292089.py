def acima_da_media(lista):
    media = sum(lista)/len(lista)
    
    lista1 = lista+[media]
    
    list.sort(lista1)
    posicao = list.index(lista1,media)
    lista_media = lista1[posicao+1:]
    
    return lista_media