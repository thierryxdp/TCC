def filtraMultiplos(lista, num):
    lista_final = []
    for item in lista:
        if (item % num) == 0:
            lista_final.append(item)
    return lista_final