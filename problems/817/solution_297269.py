def acima_da_media(lista):
    
    media=sum(lista)/len(lista)
    list.insert(lista,1,media)
    list.sort(lista)
    posicao=list.index(lista,media)
    
    
    
    
    if list.count(lista,media)>=2:
        return lista[posicao+2:]
    else:
        return lista[posicao+1:]