def acima_da_media(lista):
    mean = sum(lista) / len(lista)
    return list(filter(lambda x: x > mean, lista))