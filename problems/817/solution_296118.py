def acima_da_media(lista,n):
    
    lista=lista+[n]
    
    list.sort(lista)
    list.reverse(lista)
    
    indice=list.index[lista,n]
    
    nova_lista=lista[:indice]
    
    return nova_lista