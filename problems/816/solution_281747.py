def maiores(lista,n):
        
    sorted(lista)
    list.reverse(lista)
    
    indice= list.index(lista,n)
    
    nova_lista=lista[indice:]
    
    return nova_lista