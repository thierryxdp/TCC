def filtra_pares (a):
    lista = []
    if (a[0] % 2 == 0) == True:
        lista.append (lista[1])
    if (a[1] % 2 == 0) == True:
        lista.append (lista[2])
    if (a[2] % 2 == 0) == True:
        lista.append (lista[3])
    if (a[3] % 2 == 0) == True:
        lista.append (lista[4])
    return lista