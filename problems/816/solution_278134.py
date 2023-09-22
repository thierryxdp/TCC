def maiores(lista, n):
    
    lista1 = lista + [n]
    list.sort(lista1)
    indice = list.index(lista1, n)
    lista2 = lista1[indice:]
    
    return lista2