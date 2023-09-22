def maiores(lista,n):
    
    lista=lista+[n]
    
    sorted(lista)
    list.reverse(lista)
    
    indice= list.index(lista,n)
    
    nova_lista=lista[:indice]
    nova_lista=nova_lista- [n]
    return nova_lista