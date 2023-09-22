def maiores(lista, n):
    list.sort(lista)
    fati = list.index(lista,n)
    lista2 = lista[fati+1:]
    
    return lista2