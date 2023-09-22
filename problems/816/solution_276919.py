def maiores(lista, n):
    """Retorna uma lista contendo todos os números da lista de entradas maiores que n; lista, int -> lista."""
    if list.count(lista,n)==0:
        list.append(lista,n)
        list.sort(lista)
        list.reverse(lista)
        return lista[:list.index(lista,n)]
    else:
        list.sort(lista)
        list.reverse(lista)
        return lista[:list.index(lista,n)]