def filtra_pares(a, b, c, d):
    tupla = a, b, c, d 
    lista1 = list(tupla)
    lista2 = []
    for tupla in lista1:
        if tupla % 2 == 0:
            lista2.append(tupla)
    return lista2