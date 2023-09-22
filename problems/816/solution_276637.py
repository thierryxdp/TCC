def maiores(lista,n):
    list.sort(lista)
    var1 = list.index(n)
    del lista[0:var1+1]
    return lista