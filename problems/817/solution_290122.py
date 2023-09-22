def acima_da_media(lista):
    ordem=list.copy(lista)
    list.sort(ordem)
    notas=ordem[:-1%2]
    return notas