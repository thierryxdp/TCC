def acima_da_media(lista):
    """função que recebe uma lista com notas e retorna as notas que ficaram acima da media
    list->list"""
    z=lista
    media= sum(z)/len(z)
    list.append(z,media)
    list.sort(z)
    posmedia=list.index(z,media)
    return z[media:]