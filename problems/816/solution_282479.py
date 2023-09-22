def maiores (lista: list[int], n) -> list[int]:
    '''doc'''
    clista = lista.copy()
    clista.sort()
    clista.append(n)
    clista.sort()
    p = clista.index(n)

    listaM = clista[p+1:]

    if n in listaM:
        q = listaM.count(n)
        listaM = listaM[q:]

    return listaM