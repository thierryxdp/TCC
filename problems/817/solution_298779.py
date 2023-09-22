def acima_da_media(lista_n):
    media = sum(lista_n) / len(lista_n)
    res = list(filter(lambda x: x > media, lista_n))
    return res