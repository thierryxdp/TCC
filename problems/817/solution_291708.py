def acima_da_media(lista_notas):
    media = sum(lista_notas) / len(lista_notas)
    return maiores(lista_notas, media)