def maiores(lista,n):
    
    lista=lista+[n]
    
    sorted(lista)
    list.reverse(lista)
    
    indice= index(lista,n)
    
    nova_lista=lista[:indice]
    
    return nova_lista