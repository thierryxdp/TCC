def maiores(lista,n):
    """
    Retorna a lista dada com os numeros maiores que n ordenados em ordem crescente;
    list, int -> list
    """
    lista = lista
    lista1 = lista.sort()
    lista2 = list.index(lista,n)
    if lista2 != -1:
        return lista1[lista2:]
    else:
        return 0