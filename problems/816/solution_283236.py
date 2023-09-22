def maiores(lista,n=0):
    """
    Retorna a lista dada com os numeros maiores que n ordenados em ordem crescente;
    list, int -> list
    """
    lista = lista.sort()
    if list.index(lista,n) != -1:
        return [lista[listaIndex:]]
    else:
        return []