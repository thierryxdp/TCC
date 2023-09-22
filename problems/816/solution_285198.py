def maiores(lista,n):
    list(lista)
    lista.append(n)
    listaO = sorted(lista)
    indice = listaO.index(n)
    if n not in listaO:
        lista.append(n)
    return listaO[indice + 1:]