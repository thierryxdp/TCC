def filtra_pares(lista):
    lista1 = []
    for valor in lista:
        if lista % 2 == 0:
            lista1.append(valor)
            return lista1