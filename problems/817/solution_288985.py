def acima_da_media(media):
    lista = [number for number in media if number > sum(media)/len(media)]
    list.sort(lista)
    return lista