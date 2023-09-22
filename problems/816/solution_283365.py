def maiores(lista,n):
    
    i = len(lista)    
    list.append(lista,n)
    list.sort(lista)
    
    algarismo = list.index(lista,n)
    
    del lista[:algarismo]
    return lista