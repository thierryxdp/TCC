def maiores(lista_int,n):
    lista = []
    lista_int.append(n)
    lista_int.sort()
    lista = lista[n+1:]
    return lista