def acima_da_media(notas):
    lista_acima_da_media = []
    media = sum(notas)/len(notas)
    for n in notas:
        if n > media:
            lista_acima_da_media.append(n)
    list.sort(lista_acima_da_media)
    #print(media)
    return lista_acima_da_media