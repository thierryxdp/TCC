def filtraMultiplos(lista, num):
    i = 0
    lista_final = []
    while i < len(lista):
        if lista[i] % num == 0:
            m = lista[i]
            lista_final.append(m)
        i += 1
    return lista_final