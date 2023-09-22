def maiores(lista_inteiros, n):
    list.insert(lista_inteiros, 0, n)
    list.sort(lista_inteiros)
    lista = list.index(lista_inteiros, n)
    return lista_inteiros[lista + 1:]