def acima_da_media(lista):
    media = sum(lista)/len(lista)
    lista.append(media)
    lista.sort()
    lista = lista[lista.index(media) +1 : ]
    return lista
if lista[0]:
    return []