def maiores(lista,n):
    list.insert(lista,0,n)
    list.sort(lista)
    local_De_n = list.index(lista,n)
    lista = lista[local_De_n+1:]
    return lista