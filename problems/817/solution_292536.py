listaOrdenada = []
def acima_da_media(L):
    for i in L:
        if i > sum(L):
            listaOrdenada.append(i)
            listaOrdenada.sort()
    return listaOrdenada