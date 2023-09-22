def maiores(lista,n):
    
    lista=lista+[n]
    
    list.sort(lista)
    list.reverse(lista)
    
    indice= list.index(lista,n)
    
    nova_lista=lista[indice:]
    list.reverse(nova_lista)
    return nova_lista