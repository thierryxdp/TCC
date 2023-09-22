def acima_da_media(lista):
    media  = sum(lista)/len(lista)
    lista2 = list(filter(lambda x: x > media, lista))
    return sorted(lista2)