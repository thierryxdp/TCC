def acima_da_media(lst):
    """
    Função que retorna as notas que ficaram acima da média
    list -> list
    """

    media = sum(lst)/len(lst)
    list.append(lst, media)
    list.sort(lst)
    k = list.index(lst, media)
    nLst = lst[k+1 : ]
    return nLst