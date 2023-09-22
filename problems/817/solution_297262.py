def acima_da_media(lista):
    
    media=sum(lista)/len(lista)
    list.insert(lista,1,media)
    list.sort(lista)
    posicao=list.index(lista,media)
    
    
    
    
    if media in lista:
        return lista[posicao:]
    else:
        return lista[posicao+1:]