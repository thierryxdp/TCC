def maiores(lista, n):
    list.insert(lista,0,n)
    lista = list.sort(lista)
    return lista[n+1:]