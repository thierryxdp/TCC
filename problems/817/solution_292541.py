listaOrdenada = []
def acima_da_media(L):
    for i in L:
        if i > 3:
            listaOrdenada.append(i)
            listaOrdenada.sort()
    return listaOrdenada