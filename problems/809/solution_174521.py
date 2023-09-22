def intercala(lista1: list, lista2: list) -> list:
    """Dadas duas listas, retorna uma nova lista com os elementos das duas
       listas dadas intercalados

       Parameters:
       lista1: Primeira lista com 3 elementos
       lista2: Segunda lista com 3 elementos

       Return:
       Retorna uma nova lista com os elementos da "lista1" e da "lista2"
       intercalados

       Examples:
       intercala([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
       intercala([0, 0, 0], [0, 0, 0]) == [0, 0, 0, 0, 0, 0]
       intercala([3, 8, 11], [12, 6, 20]) == [3, 12, 8, 6, 11, 20]
    """

    return [lista1[0], lista2[0], lista1[1], lista2[1], lista1[2], lista2[2]]