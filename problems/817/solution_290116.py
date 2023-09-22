def acima_da_media(lista):
    ordem=list.copy(lista)
    list.sort(ordem)
    notas=ordem[list.index(ordem,7)]
    return notas