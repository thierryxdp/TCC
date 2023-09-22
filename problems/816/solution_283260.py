def maiores(lista,n):
    """
    Retorna a lista dada com os numeros maiores que n ordenados em ordem crescente;
    list, int -> list
    """
    lista=[3,1,2]
    lista_sort = lista.sort()
    lista_index = list.index(lista,n)
    return lista[lista_index:]