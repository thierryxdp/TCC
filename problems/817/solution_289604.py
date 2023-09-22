def acima_da_media(lista):
    media=sum(lista)/len(lista)
    
    if media in lista:
        posicao=list.index(lista,n)
        return lista[posicao+1:]
    
    if media not in lista:
        lista.append(n)
        list.sort(lista)
        posicao=list.index(lista,n)
        return lista[posicao+1:]