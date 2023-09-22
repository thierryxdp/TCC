def acima_da_media(lista):
    media=sum(lista)/len(lista)
    
    if media in lista:
        posicao=list.index(lista,media)
        list.sort(lista)
        return lista[posicao+1:]
    
    if media not in lista:
        lista.append(media)
        list.sort(lista)
        posicao=list.index(lista,media)
        return lista[posicao+1:]