def acima_da_media(lista):
    
    media=sum(lista)/len(lista)
    if media in lista:
    list.insert(lista,1,media)
    list.sort(lista)
    
    posicao=list.index(lista,media)
    
    
        return lista[posicao+2:]
    else:
        return lista[posicao+1:]