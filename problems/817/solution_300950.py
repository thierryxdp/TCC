def acima_da_media(lista):
    mean = sum(lista) / len(lista)
    lista = list(filter(lambda x: x > mean, lista))
    lista.sort()
    return lista