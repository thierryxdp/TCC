def maiores(lista,n):
    
    list.insert(lista,0,n)
    list.sort(lista)
    k = list.index(lista,n)
    lista2 = lista[k:]
    
    return lista2