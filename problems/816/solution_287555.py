def maiores(lista,n):
    lista += [n]
    list.sort(lista)
    y = lista.index(n) 
    del lista[:y+1]
    return lista