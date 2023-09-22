def maiores(lista,n):
    """"""
    list.insert(lista,0,n)
    list.sort(lista)
    lugar = list.index(n)
    listaF = lista[lugar+1:]
    return listaF