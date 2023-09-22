def maiores(lista,n):
    lista.insert(0,n)
    lista.sort()
    p=lista.index(n)
    lista1=lista[p+1:]
    return lista1