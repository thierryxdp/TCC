def acima_da_media(listaNotas):
    copiaLista=listaNotas[:]
    copiaLista.sort()
    copiaLista.reverse()
    i=copiaLista.inde(media)
    return media copiaLista[:i][::-1]