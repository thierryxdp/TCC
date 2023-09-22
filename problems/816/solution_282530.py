def maiores(lista,n):
    """"""
    lista.insert(n,0)
    lista.sort()
    ListaF = lista[n+1:]
    return ListaF