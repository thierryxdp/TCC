def maiores(lista,n):
    
    list.sort(lista)    
    del lista[:n]
    return lista