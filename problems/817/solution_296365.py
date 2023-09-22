def acima_da_media(lst):
    """
    Função que retorna as notas que ficaram acima da média
    list -> list
    """

    if len(lst) == 1:
        return []

    media = sum(lst)/len(lst)
    list.append(lst, media)
    list.sort(lst)
    k = list.index(lst, media)
    nLst = lst[k+1 : ]

    if (int(nLst[0]) in lst) and (int(nLst[0] == media)):
        del nLst[0]

    return nLst