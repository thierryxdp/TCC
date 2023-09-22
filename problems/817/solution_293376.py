def acima_da_media(listaNotas):
    copiaLista=listaNotas[:]
    copiaLista.sort()
    copiaLista.reverse()
    i=copiaLista.index(acima_da_media)
    return copiaLista