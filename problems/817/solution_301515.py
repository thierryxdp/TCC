def acima_da_media(ls):
    """Função que retorna notas que ficaram acima da média.
    assinatura: list --> list
    """
    if len(ls) == 1:
        return []
    media = (sum(ls))/len(ls)
    list.append(ls,media)
    list.sort(ls)
    return ls[list.index(ls,media) + 1:]