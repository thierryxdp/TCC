def acima_da_media(lista):
    lista=lista1
    media=sum(lista)/len(lista)
    list.insert(lista,1,media)
    list.sort(lista)
    posicao=list.index(lista,media)
    
    
    
    
    if media in lista1:
        return lista[posicao+2:]
    else:
        return lista[posicao+2:]