listaOrdenada = []
def acima_da_media(L):
    for i in L:
        if i > 7:
            listaOrdenada.append(i)
            listaOrdenada.sort()
    return listaOrdenada