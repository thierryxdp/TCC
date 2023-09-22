def filtraMultiplos(lista, n):
    return list(filter(lambda numero: numero%n == 0, lista))