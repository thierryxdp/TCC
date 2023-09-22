def maiores(lista,n):
    
    lista=list.sort(lista)
    del lista[:n]
    return lista