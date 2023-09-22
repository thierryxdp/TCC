def filtra_pares(x, y, z, w):
    lista1 = [x, y, z, w]
    lista2 = []
    for valor in lista1:
        if valor % 2 == 0:
            lista2.append(valor)
    return lista2