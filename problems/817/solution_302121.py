def acima_da_media(notas):
    media_lista = list()
    media = sum(notas)/len(notas)
    for n in notas:
        if n>media:
            media_lista.append(n)
    media_lista.sort()
    return media_lista