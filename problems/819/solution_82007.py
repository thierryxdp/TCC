def filtra_multiplos(listaNumeros, n):
    "Filtra múltiplos de um número n"
    i=0
    lista = []
    while i < len(listaNumeros):
        if listaNumero[i] % n == 0:
            lista.append(listaNumero[i])
        i += 1
    return lista