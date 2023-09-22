def acima_da_media(lista):
    lista.sort()
    media=sum(lista)//len(lista)
    posicao=list.index(lista,media)
    
    
    
    
    
    return lista[posicao+1:]