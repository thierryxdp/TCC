def maiores(lista,n):
    lista += [n]
    list.sort(lista)
    y = lista.index(n) 
    del lista[:y]
    return lista