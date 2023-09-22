def maiores(lista,n):
    
    lista=lista+[n]
    
    sorted(lista)
    list.reverse(lista)
    
    indice= list.index(lista,n)
    list.remove(lista)
    nova_lista=lista[indice:]
    
    return nova_lista