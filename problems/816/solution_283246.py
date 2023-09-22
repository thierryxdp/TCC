def maiores(lista,n):
    """
    Retorna a lista dada com os numeros maiores que n ordenados em ordem crescente;
    list, int -> list
    """
    lista0 = lista.sort()
    lista1 = list.index(lista0,n)
    return [lista[lista1:]]