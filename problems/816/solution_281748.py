def maiores(lista,n):
    lista=lista
    sorted(lista)
    list.reverse(lista)
    
    indice= list.index(lista,n)
    
    nova_lista=lista[indice:]
    
    return nova_lista