def maiores(lista, n):
    
    lista1 = lista + [n]
    list.sort(lista1)
    
    mult = list.count(lista1, n)
    indice = list.index(lista1, n)
    lista2 = lista1[indice + mult:]
    
    return lista2