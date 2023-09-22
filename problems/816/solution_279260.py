def maiores (lista_inteiros, n):
    list.insert (lista_inteiros, 0, n)
    list.sort (lista_inteiros)
    x = list.index (lista_inteiros, n)
    del lista_inteiros [:x+1]
    return lista_inteiros