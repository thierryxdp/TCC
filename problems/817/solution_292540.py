listaOrdenada = []
def acima_da_media(L):
    for i in L:
        if i > 5:
            listaOrdenada.append(i)
            listaOrdenada.sort()
    return listaOrdenada