def maiores(lista,n):
    
    lista=lista+[n]
    
    sorted(lista)
    list.reverse(lista)
    
    indice= list.index(lista,n)
    
    nova_lista=inverso[:indice]
    
    return nova_lista