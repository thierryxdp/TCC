def maiores(lista,n):
    lista1 = lista.append(n)
    lista.sort()
    v = lista.index(n)
    return lista[v+1:]