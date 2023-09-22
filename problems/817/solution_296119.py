def acima_da_media(lista,n):
    
    lista=lista+[n]
    
    ordem=list.sort(lista)
    inverso=list.reverse(ordem)
    
    indice=list.index[inverso,n]
    
    nova_lista=inverso[:indice]
    
    return nova_lista