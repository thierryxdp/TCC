def maiores(lst, n):
    """
    Retorna os valores maiores do que o inserido dentro de uma lista
    list, float -> list
    """

    
    list.append(lst, n)
    list.sort(lst)
    k = list.index(lst, n)
    nLst = lst[k+1 : ]

    return nLst