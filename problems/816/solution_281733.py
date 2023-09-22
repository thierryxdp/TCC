def maiores(lista,n):
    
    lista=lista+[n]
    
    ordem=list.sert(lista)
    
    inverso=list.reverse(ordem)
    
    indice=list.index[inverso,n]
    
    nova_lista=inverso[:indice]
    
    return nova_lista