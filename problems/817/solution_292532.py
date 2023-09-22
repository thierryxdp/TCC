listaOrdenada = []
def acima_da_media(L,m):
    for i in L:
        if i > m:
            listaOrdenada.append(i)
            listaOrdenada.sort()
    return listaOrdenada