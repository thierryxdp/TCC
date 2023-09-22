def acima_da_media(ls):
    """ Ordena uma listade notas com base na media
    assinatura: list --> list"""
    if len(ls) == 1:
        return []
    media = (sum(ls))/len(ls)
    list.append(ls,media)
    list.sort(ls)
    return ls[list.index(ls,media) + 1:]