def acima_da_media(lista):
    
    media=sum(lista)/len(lista)
    lista=list.insert(lista,1,media)
    lista.sort()
    posicao=list.index(lista,media)
    
    
    
    
    
    return lista[posicao+1:]