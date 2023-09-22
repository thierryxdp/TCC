def maiores(lista,n):
    """
    Retorna a lista dada com os numeros maiores que n ordenados em ordem crescente;
    list, int -> list
    """
    lista_sort = lista.sort()
    lista_index = list.index(lista,n)
    return lista_sort[lista_index:]