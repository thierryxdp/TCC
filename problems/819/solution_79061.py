def filtraMultiplos( lista, n):
    listaMultiplos = list(filter( lambda x: x%n == 0, lista))

    return listaMultiplos