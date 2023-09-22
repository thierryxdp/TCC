def maiores(lista_int,n):
    lista = []
    lista_int.append(n)
    lista_int.sort()
    n1 = lista_int.index(n)
    lista = lista_int[n1:]
    return lista