def maiores(lista, n):
    """
    Dada uma lista de números e um número n, gera uma nova lista contendo os números maiores do que n
    e os inserem dentro dessa nova lista.
    :param lista_numeros:
    :param n: int -> int
    :return: int -> int
    """
    list(lista)
    listaOrganizada = lista
    listaOrganizada.append(n)
    indiceMenor = min(listaOrganizada)
    indiceMaior = max(listaOrganizada)
    
    print(listaOrganizada)
    indiceN = listaOrganizada.index(n)

    if n < indiceMenor:
        return listaOrganizada[indiceN:]

    else:
        return []