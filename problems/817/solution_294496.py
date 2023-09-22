def acima_da_media(lista_notas):
    medias = sum(lista_notas)/len(lista_notas)
    return maiores(lista_notas, medias)