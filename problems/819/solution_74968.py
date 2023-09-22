def filtraMultiplos (lista, n):
    lista_result = []
    for elem in lista:
        if elem % n == 0:
            lista_result.append(elem)
    return lista_result