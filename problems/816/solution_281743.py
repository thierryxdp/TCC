def maiores(lista,n):
    
    lista=lista+[n]
    
    sorted(lista)
    list.reverse(lista)
    
    indice= list.index(inverso,n)
    
    nova_lista=inverso[:indice]
    
    return nova_lista