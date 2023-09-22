def acima_da_media(listaNotas):
    media=listaNotas/4
    copiaLista=listaNotas[:]
    copiaLista.sort()
    copiaLista.reverse()
    i=copiaLista.index(media)
    return copiaLista