def filtra_pares(tupla):
    a, b, c, d = tupla
    lista1 = list(tupla)
    lista2 = []
    for tupla in lista1:
        if tupla % 2 == 0:
            lista2.append(tupla)
    return lista2