def maiores(lista,n):
    lista += [n]
    list.sort(lista)
    y = list.index(n,lista) 
    del lista[:y-1]
    return lista