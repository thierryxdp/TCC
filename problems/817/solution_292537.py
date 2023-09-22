listaOrdenada = []
def acima_da_media(L):
    for i in L:
        if i > L:
            listaOrdenada.append(i)
            listaOrdenada.sort()
    return listaOrdenada