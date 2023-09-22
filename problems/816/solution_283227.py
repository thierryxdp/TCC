def maiores(lista,n):
    """
    Retorna a lista dada com os numeros maiores que n ordenados em ordem crescente;
    list, int -> list
    """
    lista = lista.sort()
    listaIndex = list.index(lista,n)
    if listaIndex != -1:
        return [lista[listaIndex:]]
    else:
        return []