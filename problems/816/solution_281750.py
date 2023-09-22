def maiores(lista,n):
    
    lista=lista+[n]
    
    sorted(lista)
    list.reverse(lista)
    
    indice= list.index(lista,n)
    list.del(lista,n)
    nova_lista=lista[indice:]
    
    return nova_lista