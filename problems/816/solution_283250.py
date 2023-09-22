def maiores(lista,n):
    """
    Retorna a lista dada com os numeros maiores que n ordenados em ordem crescente;
    list, int -> list
    """
    x = lista.sort()
    lista1 = list.index(x,n)
    return [lista[lista1:]]