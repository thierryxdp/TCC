def acima_da_media(media):
    lista = [number for number in media if number > statistics.mean(media)]
    return lista